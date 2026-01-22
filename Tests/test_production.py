'''
A file for tests for the production code.
'''
import unittest
import sys
from production import main
from io import StringIO

from production import reverse_word

class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        self.assertEqual(reverse_word("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_word(""), "")

    def test_character(self):
        self.assertEqual(reverse_word("a"), "a")

class TestCommandLine(unittest.TestCase):
    def test_command_line_output(self):  
        sys.argv = ['production.py', "this is a test"]
        
        sys.stdout = StringIO()
        
        main()

        printed_output = sys.stdout.getvalue().strip()
        
        sys.stdout = sys.__stdout__
        
        # Check the output
        self.assertEqual(printed_output, "siht si a tset")