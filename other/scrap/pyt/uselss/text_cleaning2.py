import re

def join_broken_lines(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Pattern to check for punctuation at the end of a line
    punctuation_pattern = r'[.,?!:;]$'

    joined_lines = []
    current_line = ''

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces

        if (not line and not current_line) or line.startswith('Chapter'):
            joined_lines.append(line)
        
        else:
            ends_with_punctuation = re.search(punctuation_pattern, line[-1])

            if ends_with_punctuation:
                current_line += line

                joined_lines.append(current_line)
                current_line = ''

            else:
                current_line += line


if __name__ == '__main__':
    join_broken_lines('ex_file.txt')