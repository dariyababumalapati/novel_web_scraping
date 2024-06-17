from extract_html_module_kgm import initiate_driver, wait_to_translate, copy_useful_html, scroll_to_bottom

from database_module_kgm import get_records, get_cn_records_id, set_column_by_id

from beautifulsoup_module_kgm import check_chinese_text

query_all = "SELECT * FROM kgm_urls;"
records_all = get_records(query_all)
url_all = [r[2] for r in records_all]

url = url_all[0]


driver = initiate_driver(url=url)
driver = wait_to_translate(driver)

cn_li = get_cn_records_id()

for id in cn_li:

    index = id-1
    url = url_all[index]
    print(url)
    driver.get(url)

    relay = True

    while relay:
        driver.refresh()
        scroll_to_bottom(driver)
        html_content = copy_useful_html(driver)
        
        relay = check_chinese_text(html_content, relay)

    set_column_by_id('raw_html', html_content, id)    




            