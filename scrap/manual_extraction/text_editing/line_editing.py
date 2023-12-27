import re

def remove_lines_with_prefixes(file_path_i, file_path_o, prefixes_to_remove):
    try:
        with open(file_path_i, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path_o, 'w', encoding='utf-8') as file:
            for line in lines:
                if not any(line.startswith(prefix) for prefix in prefixes_to_remove) and 'Book Bar' not in line:
                        file.write(line)
                    

    except FileNotFoundError:
        print(f"Error: File '{file_path_i}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while working with '{file_path_i}' or '{file_path_o}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def join_broken_lines(file_path_i, file_path_o):
    try:
        # Read the content of the file
        with open(file_path_i, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Pattern to check for punctuation at the end of a line
        punctuation_pattern = r'[.,?!:;"()]$'

        joined_lines = []
        current_line = ''

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespaces

            if not line or line.startswith('Chapter') or line.isspace():
                if current_line:
                    joined_lines.append(line)

                else:
                    joined_lines.append(line + '\n')

            else:
                ends_with_punctuation = re.search(punctuation_pattern, line[-1])

                if ends_with_punctuation:
                    current_line += line + '\n'

                    joined_lines.append(current_line)
                    current_line = ''

                else:
                    current_line += line + ' '

        with open(file_path_o, 'w', encoding='utf-8') as file:
            for joined_line in joined_lines:
                file.write(joined_line)

    except FileNotFoundError:
        print(f"Error: File '{file_path_i}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while working with '{file_path_i}' or '{file_path_o}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def find_broken_lines(file_path_i, file_path_o):
    # Read the content of the file
    with open(file_path_i, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Pattern to check for punctuation at the end of a line
    punctuation_pattern = r'[.,?!:;()]$'

    joined_lines = []
    current_line = ''

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces

        if not line or line.startswith('Chapter') or line.isspace():
            if current_line:
                joined_lines.append(line)

            else:
                joined_lines.append(line + '\n')

        else:
            ends_with_punctuation = re.search(punctuation_pattern, line[-1])

            if ends_with_punctuation and not current_line:
                pass

            elif ends_with_punctuation:
                current_line += line + '\n'

                joined_lines.append(current_line)
                current_line = ''

            else:
                current_line += line + ' '

    with open(file_path_o, 'w', encoding='utf-8') as file:
        for joined_line in joined_lines:
            file.write(joined_line)

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
    print('line_editing.py module is running in main.')
