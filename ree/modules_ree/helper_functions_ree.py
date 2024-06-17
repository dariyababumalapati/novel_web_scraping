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

# Provide the file path to delete

if __name__ == '__main__':
    print('helper_functions.py running in main.')