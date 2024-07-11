def remove_content_between_keywords(file_path, f_p, start_keyword, end_keyword):
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the start and end indices of keyword pairs and remove the content between them
    while True:
        start_index = content.find(start_keyword)
        end_index = content.find(end_keyword, start_index + len(start_keyword))
        
        if start_index != -1 and end_index != -1:
            # Delete the content between the keywords along with the keywords themselves
            content = content[:start_index] + content[end_index + len(end_keyword):]
            print(start_index, end_index)
        else:
            break

    # Write the modified content back to the file
    with open(f_p, 'w', encoding='utf-8') as file:
        file.write(content)

# Usage:
file_path = 'example_raw_html.html'  # Replace with your file path
f_p = 'z.html'
start_keyword = 'UU'
end_keyword = 'et'

remove_content_between_keywords(file_path, f_p, start_keyword, end_keyword)
