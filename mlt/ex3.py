from bs4 import BeautifulSoup

# Read the HTML from "htmls/ch_list_html.html"
with open("mlt/htmls/ch_list_html.html", "r", encoding='utf-8') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Prettify the HTML
pretty_html = soup.prettify()

# Store the prettified HTML in "htmls/ch_outer.html"
with open("mlt/htmls/ch_outer.html", "w", encoding='utf-8') as file:
    file.write(pretty_html)