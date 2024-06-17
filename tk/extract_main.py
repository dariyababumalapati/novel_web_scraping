import json
from bs4 import BeautifulSoup
from bs4_html_module import extract_chapter_html, convert_html_to_xhtml, replace_words_in_html
import time

from extract_module import initiate_driver, update_chapter_number

# Read from 'tk/jsons/ch_links.json'
with open('tk/jsons/ch_links.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

start_number = 43

stop_number = 60

update_chapter_number(stop_number)

replace_words = {'’': "'"}

chapters_data = {}

intial_url = 'https://www.mtlnovel.com/the-king/chapter-1-through-no-1/'

output_file = f'tk/jsons/chapters_data_{stop_number}.json'


for key, url in list(data.items())[start_number:stop_number+1]:
    driver = initiate_driver(url)
    driver.implicitly_wait(10)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")
    # print(soup.prettify())
    html = extract_chapter_html(soup.prettify())
    html = replace_words_in_html(html, replace_words)
    xhtml = convert_html_to_xhtml(html)
    chapters_data[key] = xhtml


# Write chapters_data to f'tk/jsons/chapters_data{x}.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chapters_data, file, ensure_ascii=False, indent=4)

driver.quit()

# url = "https://www.uuks.org/b/53573/669662.html"
# translated_url = f"https://translate.google.com/translate?sl=auto&tl=es&u={url}"

# url = 'https://www.mtlnovel.com/the-king/chapter-5-knight-squire-no-5/'


# driver = initiate_driver(url)

# # Wait for the page to finish translation
# # wait_to_translate(driver)

# driver.implicitly_wait(10)

# page_source = driver.page_source

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(page_source, "html.parser")

# # Save the soup to an HTML file
# with open("tk/htmls/output2.html", "w", encoding="utf-8") as file:
#     file.write(soup.prettify())

# # print("HTML content saved to output2.html")
