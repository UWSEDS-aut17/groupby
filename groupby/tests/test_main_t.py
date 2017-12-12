import unittest
from groupby.main import validate_args, open_files, build_report


class GroupbyTest(unittest.TestCase):
        
    # groupby.main.validate_args()
        
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
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', 'pure', 'utter', 
                       'nonsense']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Wrong option provided (not -T, -F, -L or -C)')

    def test_validate_args_fails_5(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', '-C', 
                       'path/to/calendar', '-L']
        val = validate_args(failing_arg)
        self.assertEqual(val, 'Incomplete option:argument pair')

    def test_validate_args_fails_6(self):
        failing_arg = ['groupby.py', '-F', 'path/to/Facebook', '-C']
        val = validate_args(failing_arg)
        self.assertEqual(val, "Incomplete option:argument pair")

    def test_validate_args_succeeds_1(self):
        successful_arg = ['groupby.py', '-C', 'path/to/calendar', '-F', 
                          'path/to/Facebook']
        val = validate_args(successful_arg)
        self.assertEqual(val, None)

    # groupby.main.open_files()
    
    def test_open_files_twitter_fails(self):
        failing_arg = ['groupby.py', '-T', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val[1][0], "Can't read Twitter data")       

    def test_open_files_linkedin_fails(self):
        failing_arg = ['groupby.py', '-L', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val[1][1][0], "Can't read LinkedIn data")   

    def test_open_files_facebook_fails(self):
        failing_arg = ['groupby.py', '-F', 'fake/path']
        val = open_files(failing_arg)
        self.assertEqual(val[1][2][0], "Can't read Facebook data")       

    def test_open_files_gcal_fails(self):
        failing_arg = ['groupby.py', '-T', 'data', '-C', 'fake/file.ics']
        val = open_files(failing_arg)
        self.assertEqual(val[1][3], "Can't read Google Calendar data")       
                
    def test_open_files_twitter_succeeds(self):
        successful_arg = ['groupby.py', '-T', 'data']
        val = open_files(successful_arg)
        self.assertEqual(val[2][0], True)

    def test_open_files_linkedin_succeeds(self):
        successful_arg = ['groupby.py', '-L', 'data']
        val = open_files(successful_arg)
        self.assertEqual(val[2][1], True)

    def test_open_files_facebook_succeeds(self):
        successful_arg = ['groupby.py', '-F', '~/Projects/CSE-583/CSE 583 - Team project /Facebook']
        val = open_files(successful_arg)
        self.assertEqual(val[2][2], True)

    def test_open_files_multiple_files_succeed(self):
        successful_arg = ['groupby.py', '-T', 'data', '-C', 
                          'data/shsher@uw.edu.ics']
        val = open_files(successful_arg)
        #self.assertEqual(val[0], "File(s) loaded successfully")
        self.assertEqual(val[2][3], True)

    # groupby.main.build_report()

    def test_build_report_twitter_succeeds(self):
        successful_arg = ['groupby.py', '-T', 'data']
        data = open_files(successful_arg)
        val = build_report(successful_arg, data[1])
        self.assertEqual(val[0], "Report generated successfully")

    def test_build_report_multiple_succeeds(self):
        successful_arg = ['groupby.py', '-T', 'data', '-C', 'data/shsher@uw.edu.ics', '-F', 'data']
        data = open_files(successful_arg)[1]
        val = build_report(data)
        self.assertEqual(val, "Report generated successfully")
   
if __name__ == '__main__':
    unittest.main()