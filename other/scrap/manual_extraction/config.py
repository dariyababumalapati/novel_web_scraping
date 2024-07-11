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
<<<<<<<< HEAD:other/scrap/manual_extraction/config.py
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


========
    "'": ['’'],
    '"': ['“', '”'],
    '...': ['——'],
    'Theonia': ['Dionia', 'Dionysia'],
    'Crotokatax': ['Clotocathax'],
    'Croto': ['Clotho'],
    'Leotychides': ['Leotizides'],
    'Seclian': ['Cyklian'],
    'Davos' : ['Davers', 'Daves'],
    'Thuri' : ['Tuliyi'],
}

if __name__ == '__main__':
    print('variab')
>>>>>>>> dca2e1185edd59f6ea541d656791141560c15841:other/driver_extraction/extracting_htmls/variab.py
