from modules_ree.extract_html_module_ree import *

from modules_ree.database_module_ree import *


query_all = "SELECT * FROM ree_urls;"
records_all = get_records(query_all)

url = records_all[0][2]

driver = initiate_driver(url=url)
wait_to_translate(driver)

for record in records_all[101:200]:

    chapter_id = record[0] 
    url = record[2]

    driver.get(url)
    scroll_to_bottom(driver)

    html_content = copy_useful_html(driver)

    set_column_by_id('raw_html', html_content, chapter_id)
