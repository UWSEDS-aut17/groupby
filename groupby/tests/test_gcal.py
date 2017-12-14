import pandas as pd
import mock
import unittest
from groupby import gcal


class GCalTest(unittest.TestCase):
    df = pd.DataFrame([[1, 2, 2017, 5, "A", 60], [2, 3, 2017, 5, "C", 60], [4, 5, 2017, 5, "B", 60], [5, 7, 2017, 5, "D", 600]],
                      columns=['day', 'month', 'year', 'hour', 'event_name', 'duration'])
    date_df = pd.DataFrame([[1, 2, 2015], [12, 12, 2017]], columns=['day', 'month', 'year'])

    @mock.patch('groupby.gcal')
    def test_process_calendar(self, MockOS):
        mock_os = MockOS()
        mock_os._process_calendar.return_value = self.df
        cal_df = mock_os._process_calendar("anypath")
        self.assertIsNotNone(cal_df)


    def test_plot(self):
        plot = gcal.get_plots(self.df)
        self.assertIsNotNone(plot)

    def test_get_cal_dates(self):
        cal_dates = gcal.get_cal_dates(self.date_df)
        self.assertIsNotNone(cal_dates)


if __name__ == '__main__':
    unittest.main()
