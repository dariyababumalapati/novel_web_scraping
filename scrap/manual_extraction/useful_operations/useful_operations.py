import os

def remove_files(file_path_1, file_path_2=None):
    try:
        os.remove(file_path_1)
        if file_path_2:
            os.remove(file_path_2)
        print("Files removed successfully")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")


if __name__ == "__main__":
    file_p_1 = 'text_files/extracted_text.txt'
    file_p_2 = 'text_files/dummy_file.txt'

    remove_files(file_path_1=file_p_1, file_path_2=file_p_2)
