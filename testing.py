class TweetDay:
    def __init__(self, date, sentiment):
        self.date = date
        self.sentiment = sentiment

    def get_date(self):
        return self.date

    def get_sentiment(self):
        return self.sentiment


def get_sentiment(name):
    sentiments = []

    sentiments.append(TweetDay('2019-02-24',0.06650384199134199))
    sentiments.append(TweetDay('2019-02-25',0.050742334054834075))
    sentiments.append(TweetDay('2019-02-26',0.1294559365981241))
    sentiments.append(TweetDay('2019-02-27',0.021237689393939392))
    sentiments.append(TweetDay('2019-02-28',0.07731527326839827))
    sentiments.append(TweetDay('2019-03-01',0.015951298701298695))
    sentiments.append(TweetDay('2019-03-02',0.09849242424242427))
    sentiments.append(TweetDay('2019-03-03',0.07939118867243869))

    return sentiments
