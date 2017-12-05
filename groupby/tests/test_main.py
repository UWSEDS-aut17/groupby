
import unittest
from groupby.main import validate_args, open_files, build_report


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
        
    # Interpreting arguments
        
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
        

    # Opening files
    
    def test_open_files_twitter_fails(self):
        failing_arg = ['groupby.py', '-T', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val, "Can't read Twitter data")       

    def test_open_files_linkedin_fails(self):
        failing_arg = ['groupby.py', '-L', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val, "Can't read LinkedIn data")       

    def test_open_files_facebook_fails(self):
        failing_arg = ['groupby.py', '-F', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val, "Can't read Facebook data")       

    def test_open_files_gcal_fails(self):
        failing_arg = ['groupby.py', '-T', 'data', '-C', 'fake/file.ics']
        val = open_files(failing_arg)
        self.assertEqual(val, "Can't read Google Calendar data")       
        
   
if __name__ == '__main__':
    unittest.main()