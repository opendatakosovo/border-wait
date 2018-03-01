import tweepy, os, requests, random, sys, time, unicodedata
from borderwait import message_generator
reload(sys)
sys.setdefaultencoding('utf-8')

# Tweet about the new item
class TwitterPipeline(object):
    def __init__(self, tw_consumer_key, tw_consumer_secret, tw_access_token, tw_access_token_secret, tw_gifs, path_to_gifs, feelings):
        self.tw_consumer_key = tw_consumer_key
        self.tw_consumer_secret = tw_consumer_secret
        self.tw_access_token = tw_access_token
        self.tw_access_token_secret = tw_access_token_secret
        self.tw_gifs = tw_gifs
        self.path_to_gifs = path_to_gifs
        self.feelings = feelings
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            tw_consumer_key=crawler.settings.get('TWITTER_CONSUMER_KEY'),
            tw_consumer_secret=crawler.settings.get('TWITTER_CONSUMER_SECRET'),
            tw_access_token=crawler.settings.get('TWITTER_ACCESS_TOKEN'),
            tw_access_token_secret=crawler.settings.get('TWITTER_ACCESS_TOKEN_SECRET'),
            tw_gifs=crawler.settings.get('WAIT_TIME_GIF_URLS'),
            path_to_gifs=crawler.settings.get('GIFS_DIRECTORY'),
            feelings=crawler.settings.get('FEELINGS')
        )

    # Authenticating Twitter Account and gettting the Twitter API Access
    def open_spider(self, spider):
        tw_auth = tweepy.OAuthHandler(self.tw_consumer_key, self.tw_consumer_secret)
        tw_auth.set_access_token(self.tw_access_token, self.tw_access_token_secret)
        self.tweepy_api = tweepy.API(tw_auth)

    def close_spider(self, spider):
        pass

    # Processing the item data being scraped
    def process_item(self, item, spider):
        border = item['border'].replace(' ', '')
        entry_min = item['entry']['min']
        entry_max = item['entry']['max']
        exit_min = item['exit']['min']
        exit_max = item['exit']['max']

        """
            Takes max or min numbers from the item being processed,
            will compare the parameters with min and max numbers set in feelings data in settings,
            returns a string based on values after the compare ("great", "ok", "bad")
        """
        def get_feeling(max_min):
            feeling = ['great','ok','bad']
            feeling_great_max = self.feelings['great']['max'] # by default: 30
            feeling_ok_min = self.feelings['ok']['min'] # by default: 30
            feeling_ok_max = self.feelings['ok']['max'] # by default: 60
            feeling_bad_min = self.feelings['bad']['min'] # by default: 61

            # Comparing set min and max values with item's min and max
            if max_min <= feeling_great_max:
                return feeling[0]
            elif feeling_ok_min < max_min and max_min <= feeling_ok_max:
                return feeling[1]
            elif max_min >= feeling_bad_min:
                return feeling[2]
            else:
                feeling[0]

        """
            Getting as parameter the string feeling from get_feeling definition and the border name,
            will find the gif based on the feeling and border name,
            returns exact path of gif in string
        """
        def get_feeling_path(feeling, border_name):
            # Building the path based on border name and feeling
            normalized_border_name = unicodedata.normalize("NFD", border_name).encode("ascii", "ignore")
            filename = normalized_border_name + '_' + feeling + '.gif'
            gif_filename = filename.decode('utf-8')
            return '%s/%s/%s'%(self.path_to_gifs, feeling, gif_filename)

        """
            Path of gif, generated message will be required to tweet a post in twitter feed
        """
        def tweet_gif(path, message):
            self.tweepy_api.update_with_media(path, status=message)


        # Getting the feeling based on entry max and exit max from the item being processed
        entry_feeling = get_feeling(entry_max)
        exit_feeling = get_feeling(exit_max)

        # if entry feeling is same as exit feeling tweet one post
        if entry_feeling is exit_feeling:
            # Generate 1 tweet message for both entry and exit.
            gif_path = get_feeling_path(entry_feeling, border)
            tw_message = message_generator.enter_exit(border, entry_min, entry_max, exit_min, exit_max)

            # tweet
            tweet_gif(gif_path, tw_message)
        else:
            # Generate 2 tweet messages: one for entry and one for exit.
            gif_path_entry = get_feeling_path(entry_feeling, border)
            gif_path_exit = get_feeling_path(exit_feeling, border)

            tw_message_entry = message_generator.enter(border, entry_min, entry_max)
            tw_message_exit = message_generator.exit(border, exit_min, exit_max)

            # tweet
            tweet_gif(gif_path_entry, tw_message_entry)
            tweet_gif(gif_path_exit, tw_message_exit)
        # time.sleep(60)
        return item
