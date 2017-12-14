import pandas as pd
import mock
import unittest
import datetime

class FacebookTest(unittest.TestCase):
    df = pd.DataFrame([[1, 2, 2015], [12, 12, 2017], [12, 12, 2017]],
                      columns=['id', 'month', 'year'])
    days=12
    month=12
    year=2017
    date=datetime.datetime(year,days,month)


    @mock.patch('groupby.facebook')
    def test_clean_timeline(self, MockOS):
        mock_os = MockOS()
        mock_os.clean_timeline.return_value = self.days,self.month,self.year,self.date
        days, month, year, date = mock_os.clean_timeline("anypath")
        self.assertIsNotNone(date)

    @mock.patch('groupby.facebook')
    def test_clean_friends(self, MockOS):
        mock_os = MockOS()
        mock_os.clean_friends.return_value = self.year
        year = mock_os.clean_friends("anypath")
        self.assertIsNotNone(year)


if __name__ == '__main__':
    unittest.main()
