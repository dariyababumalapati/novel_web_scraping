from extract_html_module_fsce import initiate_driver, wait_to_translate, copy_useful_html, get_title_text, scroll_to_bottom

from bs4_html_module import extract_chapter_html, convert_html_to_xhtml, check_chinese_text
import json

chapter_one_url = 'https://yunqi.qq.com/read/472146/1'

driver = initiate_driver(url=chapter_one_url)
wait_to_translate(driver)

chapters_data = {}

for x in range(81, 101):
    chapter_url = f'https://yunqi.qq.com/read/472146/{x}'
    driver.get(chapter_url)
    chapter_number = f'Chapter {x}'

    relay = True

    while relay:
        driver.refresh()
        scroll_to_bottom(driver)

        outer_html = copy_useful_html(driver)
        
        html_content = extract_chapter_html(outer_html)
        xhtml_content = convert_html_to_xhtml(html_content)

        chapters_data[chapter_number] = xhtml_content

        relay = check_chinese_text(html_content)

        with open('fcse/chapters_data_101.json', 'w', encoding='utf-8') as f:
            json.dump(chapters_data, f, ensure_ascii=False, indent=4)



driver.quit()