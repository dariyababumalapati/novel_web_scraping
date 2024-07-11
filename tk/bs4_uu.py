from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

# URL of the website
url = "https://m.uuks.org/b/57664/72080525.html"

# Initialize the undetected Chrome driver
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

# Open the URL
driver.get(url)

# Get the page source
html_content = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Get the pretty-formatted HTML
pretty_html_content = soup.prettify()

# Print or save the HTML content
with open("website_content.html", "w", encoding="utf-8") as file:
    file.write(pretty_html_content)

print("HTML content fetched and saved successfully.")

# Close the browser
driver.quit()
