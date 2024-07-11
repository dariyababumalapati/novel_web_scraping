import requests
from bs4 import BeautifulSoup

from cleaned_text import refine_text_file

from txt_to_epub import txt_to_epub
from share_file.g_drive_upolad import upload_f_to_g_drive


chapters_range = [166, 202]

file_path = rf"C:\Users\91833\OneDrive\Desktop\books\ming\ming_{chapters_range[-1]}.txt"


def fetch_chapter(chapter_number):
    url = f"https://shanghaifantasy.com/ming-dynasty-reborn-as-zhu-yunwen-chapter-{chapter_number}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve chapter {chapter_number}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    clean_paragraphs = []
    discard = False  # Flag to indicate when to start discarding paragraphs
    ignore_phrases = ["Previous", "Next", "Fiction Page"]  # Phrases that trigger removal of a paragraph

    for p in paragraphs:
        paragraph_text = p.get_text()
        if 'Dear Readers' in paragraph_text:
            discard = True  # Set the flag when 'Dear Readers' is found
        if discard:
            continue  # Skip this paragraph and all following it
        if any(phrase in paragraph_text for phrase in ignore_phrases):
            continue  # Skip paragraphs containing any of the ignore phrases
        clean_paragraphs.append(paragraph_text)

    return clean_paragraphs


def main():
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for chapter_number in range(chapters_range[0], chapters_range[-1]):  # Adjust range as needed
                try:
                    html_content = fetch_chapter(chapter_number)
                    if html_content:
                        paragraphs = parse_html(html_content)
                        for para in paragraphs:
                            file.write(para + "\n")  # Add a newline for better readability
                        file.write("\n---\n")  # Optionally, add a separator between chapters
                except Exception as e:
                    print(f"An error occurred while processing chapter {chapter_number}: {e}")
    except IOError as e:
        print(f"Failed to open or write to file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()

    ming = "11sbPdj5jBxVf76ddkIvCjU3ASBKdlKT4"

    file_name = rf"C:\Users\91833\Downloads\ming_{chapters_range[-1]}.epub"


    # upload_f_to_g_drive(file_name=up_file_path, folder_id=ree_texts)
    txt_to_epub(file_path)
    upload_f_to_g_drive(file_name=file_name, folder_id=ming)
