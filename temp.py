import json

li = ['1', '2']

def store_the_numbers(li:list): 

    first_number = li[0]

    second_number = li[-1]

    url_dict = {first_number: first_number, second_number: second_number}

    with open('numbers.json', 'a', encoding='utf-8') as f:
        json.dump(url_dict, f, indent=4)


store_the_numbers(li)