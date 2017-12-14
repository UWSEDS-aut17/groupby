import pandas as pd
import mock
import unittest
from groupby import twitter


class TwitterTest(unittest.TestCase):

    df = pd.DataFrame([[1, 2, 2015], [12, 12, 2017],[12, 12, 2017]], columns=['tweet_id', 'retweeted_status_id', 'year'])

    @mock.patch('groupby.twitter')
    def test_open_tweets(self, MockOS):
        mock_os = MockOS()
        mock_os.open_tweets.return_value = self.df
        cal_df = mock_os.open_tweets("anypath")
        self.assertIsNotNone(cal_df)


    def test_tweet_explore(self):
        unique_tweets, retweeted = twitter.tweet_explore(self.df)
        self.assertEqual(unique_tweets,2)
        self.assertEqual(retweeted, 2)

    # def test_get_cal_dates(self):
    #     cal_dates = gcal.get_cal_dates(self.date_df)
    #     self.assertIsNotNone(cal_dates)


if __name__ == '__main__':
    unittest.main()
