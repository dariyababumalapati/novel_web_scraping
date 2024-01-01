# from beautifulsoup_module_kgm import check_chinese_text
from bs4 import BeautifulSoup


with open('z.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <p> elements
p_elements = soup.find_all('p')

chinese_text_present = False

for p in p_elements:
    # Check if <p> has no children
    if len(list(p.children)) == 0:
        chinese_text_present = True
        break  # Exit the loop if Chinese text is found

if chinese_text_present:
    print("Chinese text is present in at least one <p> element.")
else:
    print("No Chinese text found in <p> elements.")
