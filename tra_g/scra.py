import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = "https://www.example.com"

u2 = "https://translate.google.com/translate?sl=auto&tl=es&u=http://example.com"

# Send a GET request to the website
response = requests.get(u2)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Save the soup to an HTML file
    with open("tra_g/htmls/output2.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
        
    print("HTML content saved to output.html")
else:
    print("Failed to retrieve the website content.")