import re


file_p = 'ex1.txt'
file_p_o = 'ex3.txt'


def join_lines(file_path, mod_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # for line in lines:
        # print(line)
    
    print(lines)

    with open(mod_file_path, 'w', encoding='utf-8') as file:

        for index, line in enumerate(lines):
            file.write(line)
            if line.strip() == '':
                print(index)
            
join_lines(file_path=file_p, mod_file_path=file_p_o)

