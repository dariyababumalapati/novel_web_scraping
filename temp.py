def remove_text_from_file(file_path, text_to_remove):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove occurrences of the specified text
        updated_content = content.replace(text_to_remove, '')

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Occurrences of '{text_to_remove}' removed from {file_path}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found")

# Specify the file path and text to remove
file_path = "C:/Users/91833/OneDrive/Desktop/books/kgm163-188.txt"  # Replace with your file path

texts_to_remove = ['www.uukanshu.', 'UU Reading', '.net'] 

for text in texts_to_remove:
# Remove the specified text from the file
    remove_text_from_file(file_path, text)


def remove_lines_starting_with(file_path, starting_text):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Remove lines starting with the specified text
        updated_lines = [line for line in lines if not line.startswith(starting_text)]

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        
        print(f"Lines starting with '{starting_text}' removed from {file_path}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found")


# file_path = "C:/Users/91833/OneDrive/Desktop/books/kgm126.txt"  # Replace with your file path
# # Specify the file path and starting text of the line to remove
# starting_text = 'Close'


# # Remove lines starting with the specified text from the file
# remove_lines_starting_with(file_path, starting_text)


