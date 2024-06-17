from bs4 import BeautifulSoup
import json

# Read from 'tk/htmls/ch_links.html' to links_code
with open("tk/htmls/ch_links.html", "r", encoding="utf-8") as file:
    links_code = file.read()

soup = BeautifulSoup(links_code, "html.parser")

# Get all the <a> tags from the soup
a_tags = soup.find_all('a')
links_dict = {a_tag.strong.text.strip(): a_tag['href'] for a_tag in a_tags}

# Save the dictionary to a JSON file
with open("tk/jsons/ch_links.json", "w", encoding="utf-8") as file:
    json.dump(links_dict, file, ensure_ascii=False, indent=4)

# # Get the text from each <a> tag
# a_texts = [a_tag.text for a_tag in a_tags]

# # Print the text of each <a> tag
# for a_text in a_texts[:1]:
    
#     ch_title = a_text
# # Print the href attribute of each <a> tag
# for a_tag in a_tags[:1]:
#     print(a_tag['href'])


# # # Save the soup to an HTML file
# # with open("tk/htmls/ch_links.html", "w", encoding="utf-8") as file:
# #     file.write(soup.prettify())

# print(ch_title.strip())
