from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<html>
<head><title>Sample</title></head>
<body>
<div>Text</div>
<div>.............</div>
<div>......</div>
<div>Clotho</div>
<div>Dionia</div>
<div>......</div>
<div>Regular text</div>
<div>....Some text....</div>
</body>
</html>
'''

def replace_words_in_html(html_content, replace_words):
    soup = BeautifulSoup(html_content, 'html.parser')

    for element in soup.descendants:
        if element.name and element.name != 'script':  # Exclude 'script' elements
            for word, replacement in replace_words.items():
                if element.string and word in element.string:
                    element.string.replace_with(str(element.string).replace(word, replacement))

    print(soup)

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

replace_words_in_html(html_content, replace_words)