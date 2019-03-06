import tweepy
from textblob import TextBlob
import datetime

consumer_key = 'MLHy2MKI0k2ffXFI3pg9ihUVS'
consumer_key_secret = 'HEYyDEskWv0amZpkVzXGfjQx7XbMPf8U9dYRYv6rb7Ovs265AU'
access_token = '1021071522889457665-PgkhYIuhih50aXLzDR0cgY24uGV1gE'
access_token_secret = 'EsOzcBojSoCmrdlG3iHV7pCf9XYS19PKLaszuKDX7U6pF'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class TweetDay:
    def __init__(self, date, sentiment):
        self.date = date
        self.sentiment = sentiment

    def get_date(self):
        return self.date

    def get_sentiment(self):
        return self.sentiment


def get_sentiment(name):
    ret = []
    today = datetime.date.today()
    for i in range(8):
        j = 7 - i
        cur_date = today - datetime.timedelta(days=j)
        query = name + ' ' + 'until:' + str(cur_date)
        max_tweets = 100
        searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

        avg_sentiment = 0
        for tweet in searched_tweets:
            avg_sentiment += TextBlob(tweet.text).sentiment.polarity
        avg_sentiment /= len(searched_tweets)

        ret.append(TweetDay(str(cur_date), avg_sentiment))

    return ret


def main():
    ret = get_sentiment("@realDonaldTrump")

    for tweetday in ret:
        print(tweetday.get_date())
        print(tweetday.get_sentiment())

main()
