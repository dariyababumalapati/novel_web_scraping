import re

file_p = 'ex1.txt'
file_p_o = 'ex3.txt'


def join_lines(file_path, mod_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    corrected_lines = []

    current_line = ''

    i = 0
    while i < len(lines) - 3:
        current_line = lines[i]

        if current_line.strip() == '':
            corrected_lines.append(current_line)
            print(corrected_lines)
        elif not re.search(r'[.!?]$', lines[i]):
            current_line = lines[i].strip() + ' ' + lines[i + 2].strip()
            corrected_lines.append(current_line.strip())
            i += 3
            print(i)
        else:
            corrected_lines.append(current_line.strip())
            print(corrected_lines)
            i += 1

    if i >= len(lines) - 3:
        for line in lines[i:]:
            print(line)
            corrected_lines.append(line.strip())
    
    with open(mod_file_path, 'w', encoding='utf-8') as file:
        for corrected_line in corrected_lines:
            file.write(corrected_line)

join_lines(file_path=file_p, mod_file_path=file_p_o)