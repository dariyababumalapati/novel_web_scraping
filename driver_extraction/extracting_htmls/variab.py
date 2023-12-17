class FilePaths:
    chap_num = '901-905'
    temp_p = f'text_files/chapters/temp_file.txt'
    cleaned_file_p = f'text_files/cleaned_chapters/{chap_num}_cleaned.txt'
    broken_file_p = f'text_files/broken_lines/{chap_num}_broken.txt'


class VariablesCall:
    replacements = {
        'China': 'Central',
        'China-Europe': 'Central-Europe',
        'China-EU': 'Central-EU',
        "’": "'",
        # Add more old_word: new_word pairs as needed
    }

    prefixes_to_remove_list = ['2020-', 'Holy Roman Empire-', 'Close']

    texts_to_remove = ['update in advance', 'my motivation to write']
    replace_words = {
        '’': "'",
        '“': '"',
        '”': '"',
        '…': '...',
        '——': '...',
        'Dionia' : 'Theonia',
        'Clotocathax': 'Crotokatax',
        'Clotocathacus': 'Crotokatax',
        'Clotho' : 'Croto',
        'Leotizides' : 'Leotychides',
        'Leonticides' : '',
        'Dionysia' : 'Theonia',
        'Sekerian' : 'Seclian',
        'Cyklian' : 'Seclian',
    }
