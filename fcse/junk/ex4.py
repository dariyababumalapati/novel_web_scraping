from bs4_html_module import create_html_document, convert_html_to_xhtml
import json
import re

def convert_text_to_html(text: str) -> str:
        """
        Convert plain text to HTML format

        Args:
            text (str): plain text content

        Returns:
            str: HTML formatted content
        """
        # Escape HTML special characters
        text = re.sub(r'&', '&amp;', text)
        text = re.sub(r'<', '&lt;', text)
        text = re.sub(r'>', '&gt;', text)
        text = re.sub(r'"', '&quot;', text)
        text = re.sub(r"'", '&#39;', text)

        # Replace newlines with <br> tags for line breaks
        html_code = text.replace('\r\n', '<br>').replace('\n', '<br>')

        # Wrap content in <p> tags
        html_code = f"<p>{html_code}</p>"

        return html_code

# Load JSON file
with open('fcse/chapters_data_110.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_data = {}

for chapter_title, chapter_content in data.items():
    html_convert = convert_text_to_html(chapter_content)
    html_content = create_html_document(html_convert)
    xhtml_content = convert_html_to_xhtml(html_content)
    new_data[chapter_title] = xhtml_content

    
# Save new data to a file
with open('fcse/chapters_data_111.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)