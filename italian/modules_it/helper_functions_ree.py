import os

def create_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting the file: {e}")


def replace_between_underscore_and_extension(file_name, replacement):
    try:
        # Find the last occurrence of '_' and '.'
        last_underscore_index = file_name.rfind('_')
        file_extension_index = file_name.rfind('.')

        if last_underscore_index != -1 and file_extension_index != -1:
            if last_underscore_index < file_extension_index:  # Ensures underscore is before the extension
                # Extract the parts of the filename
                prefix = file_name[:last_underscore_index + 1]  # Include the underscore
                suffix = file_name[file_extension_index:]  # Include the file extension
        
                # Replace the substring between the last '_' and '.' with the replacement string
                new_file_name = f"{prefix}{replacement}{suffix}"
                return new_file_name
            else:
                raise ValueError("Underscore not found before the extension.")
        else:
            raise ValueError("Invalid file name format.")
    except ValueError as e:
        return str(e)      


def rename_files_dir(dir_path:str, abbr: str):
    files = os.listdir(dir_path)

    for file in files:
        if file != '__init__.py':
            old_filepath = os.path.join(dir_path, file)

            new_filename = replace_between_underscore_and_extension(file, abbr)
            new_filepath = os.path.join(dir_path, new_filename)

            os.rename(old_filepath, new_filepath)


if __name__ == '__main__':
    print('helper_functions.py running in main.')
    # rename_files_dir(r'G:\Projects\Python_projects\novel_web_scraping\italian\modules_it', 'it')
