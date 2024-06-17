from modules_ree.extract_html_module_ree import initiate_driver, wait_to_translate, copy_useful_html

url = 'https://www.uukanshu.net/b/55900/#gsc.tab=0'

driver = initiate_driver(url)

driver = wait_to_translate(driver)

url_content = copy_useful_html(driver)

attribute = {'c'}