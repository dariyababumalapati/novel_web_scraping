import pyperclip

def convert_text_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Split the text into paragraphs based on double newline
    paragraphs = text.split('\n\n')
    
   # Start the div content
    html_content = '<div id="chapter-content">\n'

    # Add each paragraph wrapped in <p> tags inside the div
    for paragraph in paragraphs:
        html_content += f'    <p>{paragraph.strip()}</p>\n'
    
    # Close the div
    html_content += '</div>'
    
    return html_content

# Path to the input text file
file_path = 'fcse/clipboard.txt'

# Convert the text file content to HTML
html_output = convert_text_to_html(file_path)

# Print the HTML output
# print(html_output)

# Save the HTML output to a file
output_html_file = 'fcse/clip_board.html'
with open(output_html_file, 'w', encoding='utf-8') as file:
    file.write(html_output)

print(f"HTML content has been saved to {output_html_file}")
