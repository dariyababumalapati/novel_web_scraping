import os

from lxml import etree

def convert_html_to_xhtml_with_path(input_folder, output_folder, output_folder_temp, s_number, e_number):
    
    for file in range(s_number, e_number + 1):
        input_file = f'{input_folder}/chapter_{file}.html'
        output_file = f"{output_folder}/chapter_{file}.xhtml"
        output_file_temp = f"{output_folder_temp}/chapter_{file}.xhtml"


        parser = etree.HTMLParser()
        tree = etree.parse(input_file, parser)

        with open(output_file, 'wb') as f:
            f.write(etree.tostring(tree, pretty_print=True, method='xml'))
        
        with open(output_file_temp, 'wb') as f:
            f.write(etree.tostring(tree, pretty_print=True, method='xml'))

def convert_html_to_xhtml(input_file_path, output_file_path, output_file_path_temp):

    parser = etree.HTMLParser()
    tree = etree.parse(input_file_path, parser)

    with open(output_file_path, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))
    
    with open(output_file_path_temp, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))


def delete_files_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through files and delete each one
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Check if it's a file
            os.remove(file_path)  # Delete the file

# Provide the folder path where you want to delete files

# Call the function to delete files in the folder


# Example usage:

if __name__ == "__main__":
    input_folder = 'files/html_files/mhag/cleaned'
    output_folder = 'files/xhtml_files/mhag'
    output_folder_temp = 'files/xhtml_files_temp/mhag'

    starting_number = 894
    ending_number = 916
    
    delete_files_in_folder(output_folder_temp)

    # convert_html_to_xhtml(input_folder=input_folder, output_folder=output_folder, output_folder_temp=output_folder_temp, s_number=starting_number, e_number=ending_number)



