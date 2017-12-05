import unittest
from groupby import validate_args


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
        failing_arg = args(failing_arg)
        self.assertEqual(val, 'Failed to provide minimum argument')

    def test_validate_args_fails_2(self):
        failing_arg = ['groupby.py', '-F']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Failed to provide minimum argument')

    def test_validate_args_fails_3(self):
        failing_arg = ['groupby.py', '-C', 'path/to/calendar']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Failed to provide minimum argument')

    def test_validate_args_fails_4(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', 'pure', 'utter', 'nonsense']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Wrong option provided (not -T, -F, -L or -C)')

    def test_validate_args_fails_5(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', '-C', 'path/to/calendar', '-L']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Incomplete option:argument pair')


    
if __name__ == '__main__':
    unittest.main()