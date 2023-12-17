import unittest
from bs4 import BeautifulSoup
from driver_extraction.extracting_htmls.beautifulsoup_editing_modules import replace_words_in_html  # Replace 'your_module_containing_function' with your module name

class TestReplaceWordsInHTML(unittest.TestCase):
    def test_replace_words_in_html(self):
        # Sample HTML content
        html_content = '''
            <html>
                <body>
                    <p>This is a sample paragraph with some words to replace.</p>
                    <div>
                        <p>Another paragraph here.</p>
                        <span>Yet another sentence.</span>
                    </div>
                </body>
            </html>
        '''
        
        # Create BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Dictionary of replacements
        replacements_dict = {
            "new_word_1": ["sample"],
            "new_word_2": ["words", "sentence"]
        }

        # Perform word replacements
        modified_soup = replace_words_in_html(soup, replacements_dict)

        # Verify replacements in the modified HTML
        expected_output = '''
            <html>
                <body>
                    <p>This is a new_word_1 paragraph with some new_word_1 to replace.</p>
                    <div>
                        <p>Another paragraph here.</p>
                        <span>Yet another new_word_2.</span>
                    </div>
                </body>
            </html>
        '''

        self.assertEqual(str(modified_soup), expected_output)

if __name__ == '__main__':
    unittest.main()
