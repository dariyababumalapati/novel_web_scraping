from txt_to_epub import txt_to_epub
from share_file.g_drive_upolad import upload_f_to_g_drive


def refine_text_file(input_path, output_path, replacement_pairs, target_string):
    try:
        # Read the original file
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        refined_lines = []

        # Process each line
        for line in lines[1:]:
            # Replace specific strings
            for old, new in replacement_pairs:
                line = line.replace(old, new)
            
            # Collect line if it does not contain the target string for deletion
            if target_string not in line:
                refined_lines.append(line)

        # Write the refined text to a new file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.writelines(refined_lines)
    
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
    except IOError:
        print("Error: An issue occurred while reading or writing files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':

    chapter_number = 250

    input_path = rf"C:\Users\91833\OneDrive\Desktop\books\ming\ming_{chapter_number}.txt"
    output_path = rf"C:\Users\91833\OneDrive\Desktop\books\ming\cleaned\ming_cleaned_{chapter_number}.txt"
    download_file_path = rf"C:\Users\91833\Downloads\ming_cleaned_{chapter_number}.epub"

    #drive folder    
    ming = "11sbPdj5jBxVf76ddkIvCjU3ASBKdlKT4"

    replacement_pairs = [('I was reborn as Zhu Yunwen-', ''), ('-69 Book Bar', '')]
    unwanted_string = 'Author: Hanmei Jingxue'

    refine_text_file(input_path, output_path, replacement_pairs, unwanted_string)

    txt_to_epub(output_path)

    upload_f_to_g_drive(file_name=download_file_path, folder_id=ming)
