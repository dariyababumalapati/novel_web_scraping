import unittest
from io import StringIO

import sys
sys.path.append('G:/Projects/Python_projects/novel_web_scraping/')
# Import the function to be tested
from text_cleaning import join_broken_lines


class TestJoinBrokenLines(unittest.TestCase):

    def test_join_broken_lines(self):
        input_text = "He woke up\n\nin the morning.\n\nHe washed his face.\n\nHe brushed his\n\nteeth cleanly.\n\nAte breakfast.\n\nTook a walk.\n\nHe came back\n\nhome."
        expected_output = "He woke up in the morning.\nHe washed his face.\nHe brushed his teeth cleanly.\n\nAte breakfast.\nTook a walk.\nHe came back home."
        
        # Create a fake file for testing input
        fake_input = StringIO(input_text)

        # Create a fake file for testing output
        fake_output = StringIO()

        # Call the function with the fake files
        join_broken_lines(fake_input, fake_output)

        # Get the content of the output fake file
        output_content = fake_output.getvalue().strip()

        # Compare the output content with the expected output
        self.assertEqual(output_content, expected_output)

if __name__ == '__main__':
    unittest.main()
