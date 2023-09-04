# Python script for extracting data from a website's responsive table
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table element with a specific ID or class name
        # Replace 'table_id' or 'table_class' with the actual ID or class name of the table
        table = soup.find("table", {"id": "table_id"})  # You can use "class" instead of "id" if applicable

        if table:
            # Iterate through the rows of the table
            for row in table.find_all("tr"):
                # Extract data from the cells (td elements) in each row
                columns = row.find_all("td")
                if columns:
                    # Extract and print the data from each cell
                    data = [column.text.strip() for column in columns]
                    print(data)

        else:
            print("Table not found on the page.")

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

if __name__ == "__main__":
    url = input("Enter the URL of the website with the responsive table: ")
    scrape_data(url)
