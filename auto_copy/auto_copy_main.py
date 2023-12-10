from auto_copy.autocopy import orienting_tabs, process_page, sav, preload_pages_same_tab

num_pages = 5
  # Change this to the number of pages you want to scrape


orienting_tabs()

preload_pages_same_tab(num_pages)

for _ in range(num_pages):
    process_page()

sav()
