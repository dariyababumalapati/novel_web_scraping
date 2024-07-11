import json
from itertools import islice

def process_and_save_dict(original_dict, replace_words_dict, file_path):
    """
    Processes the keys of a dictionary by replacing specified characters and then saves the modified dictionary to a JSON file.

    Args:
        original_dict (dict): The original dictionary whose keys need to be processed.
        replace_words_dict (dict): A dictionary where each key-value pair represents the character to replace and its replacement.
        file_path (str): The path to the JSON file where the processed dictionary will be saved.

    """
    # Copy the original dictionary to avoid modifying it directly
    temp_dict = original_dict.copy()
    
    # Initialize a new dictionary to store the modified keys and values
    new_ming_dict = {}
    
    # Iterate through the original dictionary to replace characters in the keys
    for key, value in temp_dict.items():
        new_key = key
        new_value = value

        for old_char, new_char in replace_words_dict.items():
            new_key = new_key.replace(old_char, new_char)

        for old_char, new_char in replace_words_dict.items():
            new_value = new_value.replace(old_char, new_char)

        new_ming_dict[new_key] = new_value
    print(file_path)

    # Save the modified dictionary to the specified JSON file
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     json.dump(new_ming_dict, f, indent=4)
    # print(f"Data successfully written to {file_path}")
    return new_ming_dict



def read_json_and_write_to_txt(json_file_path, txt_file_path):
    """
    Reads data from a JSON file and writes it to a text file with UTF-8 encoding.

    Args:
        json_file_path (str): The path to the JSON file.
        txt_file_path (str): The path to the output text file.
    """
    try:
        # Read data from the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Convert the data into a string format
        # Here, I'm converting the dictionary into a formatted string for example purposes
        data_string = json.dumps(data, indent=4)

        # Write the formatted string to a text file with UTF-8 encoding
        with open(txt_file_path, 'w', encoding='utf-8') as file:
            file.write(data_string)
        
        print("Data has been successfully written to", txt_file_path)
    
    except Exception as e:
        print("An error occurred:", e)

def save_json(file_path, file):
    with open (file_path, 'w', encoding='utf-8') as f:
        json.dump(file, f, indent=4)


# Example usage of the function
if __name__ == '__main__':

    replace_words_dict = {'’': "'", '”': "'", '“': "'", '\\"' : '"',}
    json_file_path = 'book_bar/c_t.json'
    txt_file_path = 'book_bar/c_t.txt'

    # read_json_and_write_to_txt(json_file_path, txt_file_path)

    with open(json_file_path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    
    for key, value in data_dict.items():
        print(key, value)

    # a = process_and_save_dict(data_dict, replace_words_dict, json_file_path)

    # for key, value in a.items():
    #     print(key, value)


