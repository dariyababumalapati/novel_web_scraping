def replace_escaped_quotes(original_dict):
    """
    Creates a new dictionary with all escaped double quotes in keys and values replaced by regular double quotes.

    Args:
        original_dict (dict): The original dictionary with potentially escaped quotes.

    Returns:
        dict: A new dictionary with replaced quotes.
    """
    new_dict = {}
    for key, value in original_dict.items():
        # Replace escaped double quotes in the key and value
        new_key = key.replace('\\"', '"')
        new_value = value.replace('\\"', '"')
        new_dict[new_key] = new_value
    return new_dict

# Example dictionary with escaped double quotes
example_dict = {
    "Chapter 1 I am Zhu Yunwen! I am the emperor of Ming Dynasty!": "https://www.69shu.pro/txt/55016/35294498",
    "Chapter 2 Zhu Di's three sons": "https://www.69shu.pro/txt/55016/35294499",
    "Chapter 3: The cards are still the same, play slowly": "https://www.69shu.pro/txt/55016/35294500",
    "Chapter 4 Xu Huizu's surprise": "https://www.69shu.pro/txt/55016/35294501",
    "Chapter 5 Fang Xiaoru, a loyal minister through the ages": "https://www.69shu.pro/txt/55016/35294502",
    "Chapter 6: Academic tycoon Jie Jin's duet": "https://www.69shu.pro/txt/55016/35294503",
    "Chapter 7 Eunuchs have a hard time": "https://www.69shu.pro/txt/55016/35294504",
    "Chapter 8: The relatives of the Ming Dynasty felt aggrieved": "https://www.69shu.pro/txt/55016/35294505",
    "Chapter 9 Select talents and open a cabinet": "https://www.69shu.pro/txt/55016/35294506",
    "Chapter 10 Dao Yan proposes a plan to King Yan, and Zhu Di prepares to go to the capital": "https://www.69shu.pro/txt/55016/35294507",
    "Chapter 11 The empire is suffering from a stubborn disease, does Li Jinglong have second thoughts?": "https://www.69shu.pro/txt/55016/35294508",
    "Chapter 12 \"The Emperor is a man of God!\"": "https://www.69shu.pro/txt/55016/35294509",
    "Chapter Thirteen: New Recruit Strategies and Business Difficulties": "https://www.69shu.pro/txt/55016/35294510",
    "Chapter 14 Ming Security Bureau": "https://www.69shu.pro/txt/55016/35294511",
}

# Replace the escaped quotes
updated_dict = replace_escaped_quotes(example_dict)

# Print the updated dictionary to verify changes
for key, value in updated_dict.items():
    print(f"{key}: {value}")

