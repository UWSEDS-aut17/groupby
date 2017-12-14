import pandas as pd
import mock
import unittest


class LinkedInTest(unittest.TestCase):
    df = pd.DataFrame([[1, 2, 2015], [12, 12, 2017], [12, 12, 2017]],
                      columns=['id', 'month', 'year'])

    @mock.patch('groupby.linkedin')
    def test_open_linkedin(self, MockOS):
        mock_os = MockOS()
        mock_os.open_linkedin.return_value = self.df
        cal_df = mock_os.open_linkedin("anypath")
        self.assertIsNotNone(cal_df)

    @mock.patch('groupby.linkedin')
    def test_import_recruiters_contacts(self, MockOS):
        mock_os = MockOS()
        mock_os.import_recruiters_contacts.return_value = self.df
        cal_df = mock_os.import_recruiters_contacts("anypath")
        self.assertIsNotNone(cal_df)


if __name__ == '__main__':
    unittest.main()
