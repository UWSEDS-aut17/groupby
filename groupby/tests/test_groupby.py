
import unittest
from groupby import validate_args, open_files, analyze_data


""" Useful code

# Path to testing data
import os.path as op
import shablona as sb
data_path = op.join(sb.__path__[0], 'data')

import subprocess
        subprocess.call(['touch', self.fname])
        subprocess.call(['rm', self.fname])

"""


class FileTest(unittest.TestCase):
        
    def test_validate_args_fails_1(self):
        failing_arg = ['groupby.py'] 
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Failed to provide minimum argument')

    def test_validate_args_fails_2(self):
        failing_arg = ['groupby.py', '-F']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Failed to provide minimum argument')

    def test_validate_args_fails_3(self):
        failing_arg = ['groupby.py', '-C', 'path/to/calendar']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Failed to provide social media data')

    def test_validate_args_fails_4(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', 'pure', 'utter', 'nonsense']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Wrong option provided (not -T, -F, -L or -C)')

    def test_validate_args_fails_5(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', '-C', 'path/to/calendar', '-L']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Incomplete option:argument pair')

    def test_validate_args_fails_6(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', '-C']
        val = validate_args(failing_arg)
        self.assertEqual(val, "Incomplete option:argument pair")

    def test_validate_args_succeeds_1(self):
        successful_arg = ['groupby.py', '-C', 'path/to/calendar', '-F', 'path/to/Facebook']
        val = validate_args(successful_arg)
        self.assertEqual(val, None)

"""
    def test_open_files_fails_1(self):
        failing_arg = ['groupby.py', '-F', 'data/fake_data.html']
        val = open_files(failing_arg)
        self.assertEqual(val, "")
"""

    
if __name__ == '__main__':
    unittest.main()