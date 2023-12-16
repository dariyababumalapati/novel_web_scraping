from html_edting_modules import remove_elements_with_certain_texts, replace_words_in_html, replace_dots_with_dash


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

texts_to_remove = ['update in advance', 'my motivation to write']

starting_number = 894
ending_number = 916

for numb in range(starting_number, ending_number + 1):
    file_path_in = f'files/html_files/mhag/raw/chapter_{numb}.html'
    file_path_out = f'files/html_files/mhag/cleaned/chapter_{numb}.html'
    with open(file_path_in, 'r', encoding='utf-8') as file:
        html_content = file.read()

    mod_html = remove_elements_with_certain_texts(html_content, texts_to_remove)
    mod_html = replace_words_in_html(mod_html, replace_words)
    mod_html = replace_dots_with_dash(mod_html)

    with open(file_path_out, 'w', encoding='utf-8') as file:
        file.write(mod_html)

