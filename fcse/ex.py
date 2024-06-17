import json

# Specify the path to your JSON file
json_file_path = 'chapters_data.json'

# Open the JSON file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    # Load the JSON data
    data = json.load(json_file)

chapters_data = {}

# Loop through the data
chapter_number = 1

for title, xhtml_content in data.items():
    # Store the chapter data
    chapter_title = f'Chapter {chapter_number}'
    chapters_data[chapter_title] = xhtml_content
    chapter_number += 1

# Specify the path to the output JSON file
output_json_file_path = 'fcse/chapters_data.json'

# Dump the chapters_data into the JSON file
with open(output_json_file_path, 'w', encoding='utf-8') as output_json_file:
    json.dump(chapters_data, output_json_file, ensure_ascii=False, indent=4)