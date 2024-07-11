import json
import os
from bs4 import BeautifulSoup

# Read the HTML from "mlt/htmls/ch_list_html.html" 
with open("mlt/htmls/ch_outer.html", "r", encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

results = []

# Find all <p> tags containing <a> tags with class 'ch-link'

a_tags = soup.find_all('a', class_='ch-link')

a_tags.reverse()


# Get all the <a> tags from the soup
# a_tags = soup.find_all('a')
links_dict = {a_tag.strong.text.strip(): a_tag['href'] for a_tag in a_tags}

# Specify the file path
file_path = os.path.join('mlt', 'jsons', 'ch_links.json')

# Create directories if they do not exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Write results to the JSON file with encoding
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(links_dict, f, ensure_ascii=False, indent=4)

print(f"Data has been written to {file_path}")
