import requests, random, sys, unicodedata
from borderwait import message_generator
# reload(sys)
# sys.setdefaultencoding('utf-8')

# Post on Facebook about the new item
class FacebookPipeline(object):
    def __init__(self, fb_access_token, fb_gif_urls, feelings):
        self.fb_access_token = fb_access_token
        self.fb_gif_urls = fb_gif_urls
        self.feelings = feelings
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            fb_access_token=crawler.settings.get('FACEBOOK_ACCESS_TOKEN'),
            fb_gif_urls=crawler.settings.get('WAIT_TIME_GIF_URLS'),
            feelings=crawler.settings.get('FEELINGS')
        )

    def open_spider(self, spider):
        self.fb_auth = 'https://graph.facebook.com/me/feed?access_token='+self.fb_access_token

    def close_spider(self, spider):
        pass

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

        def get_feeling_url(feeling, border):
            normalized_border_name = unicodedata.normalize("NFD", border).encode("ascii", "ignore")
            url = "http://207.154.242.169:81/images/" + feeling + "/" + normalized_border_name + ".gif"
            return url.encode('utf-8').strip()

        def fb_gif(url, message, feeling):
            post_content = {'message': '%s' %(message), 'description': '%s' %(message),'link':str(url)}
            facebook_post = requests.post(self.fb_auth, data=post_content).text

        entry_feeling = get_feeling(entry_max)
        exit_feeling = get_feeling(exit_max)

        if entry_feeling is exit_feeling:
            # Generate 1 fb message for both entry and exit.
            gif_url = get_feeling_url(entry_feeling, border)
            fb_message = message_generator.enter_exit(border, entry_min, entry_max, exit_min, exit_max)
            # fb
            fb_gif(gif_url, fb_message, entry_feeling)
        else:
            # Generate 2 fb messages: one for entry and one for exit.
            gif_url_entry = get_feeling_url(entry_feeling, border)
            gif_url_exit = get_feeling_url(exit_feeling, border)

            fb_message_entry = message_generator.enter(border, entry_min, entry_max)
            fb_message_exit = message_generator.exit(border, exit_min, exit_max)

            # fb
            fb_gif(gif_url_entry, fb_message_entry, entry_feeling)
            fb_gif(gif_url_exit, fb_message_exit, exit_feeling)
