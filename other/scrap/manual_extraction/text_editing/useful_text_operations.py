def remove_lines_with_prefixes(file_path_i, file_path_o, prefixes_to_remove):
    try:
        with open(file_path_i, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path_o, 'w', encoding='utf-8') as file:
            for line in lines:
                if not any(line.startswith(prefix) for prefix in prefixes_to_remove):
                    file.write(line)

    except FileNotFoundError:
        print(f"Error: File '{file_path_i}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while working with '{file_path_i}' or '{file_path_o}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def replace_words_in_file(file_path, replacement_words):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        for old_word, new_word in replacement_words.items():
            content = content.replace(old_word, new_word)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while working with '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':

    # Replace 'old_word' with 'new_word' in 'example.txt'
    chap_num = '876-900'
    file_p = f'text_files/cleaned_chapters/{chap_num}_cleaned.txt'
    # file_p = f'text_files/replace_word_test.txt'

    replacements = {
    'China': 'Central',
    'China-Europe': 'Central-Europe',
    'China-EU': 'Central-EU',
    "’": "'",
    # Add more old_word: new_word pairs as needed
    }

    # word_replacement_list = [['China', 'Mainland'], ["’", "'"]]
    # replace_word_in_file(file_path=file_p, word_replace_list=word_replacement_list)
    replace_words_in_file(file_path=file_p, replacement_words=replacements)

