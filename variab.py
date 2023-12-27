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