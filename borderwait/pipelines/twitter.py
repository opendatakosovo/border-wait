import tweepy
from twitter_auth import *


# Tweet about the new item
class TwitterPipeline(object):
    def __init__(self, tw_consumer_key, tw_consumer_secret, tw_access_token, tw_access_token_secret):
        self.tw_consumer_key = tw_consumer_key
        self.tw_consumer_secret = tw_consumer_secret
        self.tw_access_token = tw_access_token
        self.tw_access_token_secret = tw_access_token_secret

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            tw_consumer_key=crawler.settings.get('TWITTER_CONSUMER_KEY'),
            tw_consumer_secret=crawler.settings.get('TWITTER_CONSUMER_SECRET'),
            tw_access_token=crawler.settings.get('TWITTER_ACCESS_TOKEN'),
            tw_access_token_secret=crawler.settings.get('TWITTER_ACCESS_TOKEN_SECRET')
        )

    def open_spider(self, spider):
        auth = tweepy.OAuthHandler(self.tw_consumer_key, self.tw_consumer_secret)
        auth.set_access_token(self.tw_access_token, self.tw_access_token_secret)
        self.tweepy_api = tweepy.API(auth)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        tweet = 'kufiri: %s hyrje: %s dalje: %s\n%s %s' % (item['border'], item['entry_q'], item['exit_q'], '#hashtag1s2', '#hashtag2')
        self.tweepy_api.update_status(status=tweet)

        return item
