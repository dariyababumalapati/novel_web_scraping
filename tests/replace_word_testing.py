import unittest
import os
import sys

sys.path.append('G:/Projects/Python_projects/novel_web_scraping/')

# Assuming the function 'replace_word_in_file' is in the 'text_operations' module
from text_editing.useful_text_operations import replace_word_in_file

class TestReplaceWordInFile(unittest.TestCase):

    def test_replace_word_in_file(self):
        # Create a temporary test file
        file_path = 'word_test.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("This is a test file with China and ’ characters.")

        # Define the word replacement list for the test
        word_replace_list = [('China', 'Mainland'), ("’", "'")]

        # Call the function to replace words in the test file
        replace_word_in_file(file_path, word_replace_list)

        # Read the modified content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            modified_content = file.read()

        # Check if the replacement was successful
        expected_content = "This is a test file with Mainland and ' characters."
        self.assertEqual(modified_content, expected_content)

        # Clean up: Delete the temporary test file
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
