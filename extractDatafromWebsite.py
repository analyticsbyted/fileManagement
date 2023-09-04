# Python script for extracting data from a website
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Extract text from all <p> tags on the page
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.text)

        # Example: Extract the title of the page (inside the <title> tag)
        title = soup.title
        if title:
            print("Title:", title.text)

        # Add more code here to extract data from other elements as needed

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

if __name__ == "__main__":
    url = input("Enter the URL of the website: ")
    scrape_data(url)
