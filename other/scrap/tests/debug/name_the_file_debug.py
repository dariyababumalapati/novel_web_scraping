import re
import os

def name_the_file():
    # file_path = "novel_text.txt"
    file_path = "zzz.txt"

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines_starting_with_chapters = [line.strip() for line in lines if line.strip().startswith('Chapter')]

        if len(lines_starting_with_chapters) >= 2:
            first_chapter = re.findall(r'\d+', lines_starting_with_chapters[0])[0]
            last_chapter = re.findall(r'\d+', lines_starting_with_chapters[-1])[0]
        
            new_file_path = f"debug/chapters_raw/{first_chapter}-{last_chapter}_raw.txt"
            print(new_file_path)
            os.rename(file_path, new_file_path)
            print(f"File renamed to {new_file_path}")
        else:
            print("Insufficient chapters to rename the file.")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to rename the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

    chapter_indexes = [first_chapter, last_chapter]
    return chapter_indexes

if __name__ == '__main__':
    # Call the function
    file_path = name_the_file()
