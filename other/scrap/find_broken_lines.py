import re

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

if __name__ == '__main__':
    
    find_broken_lines(file_path_i='ex2.txt', file_path_o='ex3.txt')
    # join_broken_lines(file_path_i='ex4.txt', file_path_o='ex3.txt')
