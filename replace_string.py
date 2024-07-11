# Define the file path
file_path = r"C:\Users\91833\OneDrive\Desktop\books\ree\ree_100.txt"

# Define the string to be replaced and the new string

string_to_replace =   ["UU Kanshu www.uukanshu.net", "UU Reading www.uukanshu. net", "UU Reading www.uukanshu. net"]
new_string = ""


# Read the file content
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Perform the replacement
for string in string_to_replace:
        modified_content = file_content.replace(string, new_string)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)
