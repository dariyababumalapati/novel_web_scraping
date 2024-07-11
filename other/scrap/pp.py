import json

def get_start_end_numbers(start_num, end_num, cycles):
        if start_num and end_num:
            start_number = int(start_num)
            end_number = int(end_num)
            print("Both start_num and end_num provided.")
        else:
            print("Either start_num or end_num is not provided.")
            with open('tk/inproject_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            start_number = data['chapter_number']
            end_number = start_number + cycles
        
        return start_number, end_number

st = 10
en = 20

cycles = 5 

a, b = get_start_end_numbers(st, en, cycles)

print(a, b)

print(a)