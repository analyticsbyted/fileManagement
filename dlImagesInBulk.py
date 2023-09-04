import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import hashlib
import imghdr  # To check the image file type

# Function to generate a unique file name for an image
def generate_unique_filename(img_url, response):
    # Extract the Content-Type from the response headers
    content_type = response.headers.get("Content-Type")

    # Determine the file extension based on Content-Type or use a default
    if content_type:
        if "image/jpeg" in content_type:
            file_extension = ".jpg"
        elif "image/png" in content_type:
            file_extension = ".png"
        else:
            file_extension = ".jpg"  # Default to .jpg if Content-Type is unknown
    else:
        file_extension = ".jpg"  # Default to .jpg if Content-Type is missing

    # Generate a hash of the image URL to ensure a unique file name
    hash_object = hashlib.md5(img_url.encode())
    return hash_object.hexdigest() + file_extension

# Function to download images to a local folder
def download_images_to_local(url, local_folder, max_images=20):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all image tags
        img_tags = soup.find_all("img")

        # Initialize a counter for downloaded images
        downloaded_images = 0

        # Download each image up to the specified limit
        for img_tag in img_tags:
            if downloaded_images >= max_images:
                break

            img_url = img_tag.get("src")
            if img_url:
                img_url = urljoin(url, img_url)  # Make sure the URL is absolute

                # Download the image to the local folder
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # Check the image file type using imghdr
                    image_type = imghdr.what(None, h=img_response.content)
                    if image_type in ("jpeg", "png"):
                        img_name = generate_unique_filename(img_url, img_response)
                        img_path = os.path.join(local_folder, img_name)
                        with open(img_path, "wb") as img_file:
                            img_file.write(img_response.content)
                        print(f"Downloaded: {img_url} => {img_path}")
                        downloaded_images += 1
                    else:
                        print(f"Skipping: {img_url} (Unsupported file type)")
                else:
                    print(f"Failed to download: {img_url}")

        print(f"Downloaded {downloaded_images} out of {max_images} images to the local folder.")

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

if __name__ == "__main__":
    url = input("Enter the URL of the webpage containing images: ")
    local_download_folder = input("Enter the local folder where you want to save the images: ")

    # Create the local_download_folder if it doesn't exist
    os.makedirs(local_download_folder, exist_ok=True)

    download_images_to_local(url, local_download_folder, max_images=20)
