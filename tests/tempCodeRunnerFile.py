import unittest
from io import StringIO
from unittest.mock import patch

import sys
sys.path.append('text_cleaning.py')
# Import the function to be tested
from text_cleaning import join_broken_lines


class TestJoinBrokenLines(unittest.TestCase):

    def test_join_broken_lines(self):
        input_text = "He woke up\n\nin the morning.\n\nHe washed his face.\n\nHe brushed his\n\nteeth cleanly.\n\nAte breakfast.\n\nTook a walk.\n\nHe came back\n\nhome."
        expected_output = "He woke up in the morning.\nHe washed his face.\nHe brushed his teeth cleanly.\n\nAte breakfast.\nTook a walk.\nHe came back home."
        
        # Create a fake file for testing
        fake_file = StringIO(input_text)

        # Patch 'open' to use the fake file
        with patch('builtins.open', return_value=fake_file, create=True):
            output = StringIO()
            with patch('sys.stdout', output):
                join_broken_lines('fake_file_path.txt')

            # Get the printed output
            printed_output = output.getvalue().strip()

            # Compare the printed output with expected output
            self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    unittest.main()
