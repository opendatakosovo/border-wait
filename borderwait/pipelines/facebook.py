import requests, random

# Post on Facebook about the new item
class FacebookPipeline(object):
    def __init__(self, fb_access_token, fb_gifs):
        self.fb_access_token = fb_access_token
        self.fb_gifs = fb_gifs
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            fb_access_token=crawler.settings.get('FACEBOOK_ACCESS_TOKEN'),
            fb_gifs=crawler.settings.get('WAIT_TIME_GIF_URLS')
        )

    def open_spider(self, spider):
        self.fb_url = 'https://graph.facebook.com/me/feed?access_token='+self.fb_access_token

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        border = item['border']
        entry_min = item['entry']['min']
        entry_max = item['entry']['max']
        exit_min = item['exit']['min']
        exit_max = item['exit']['max']

        def get_feeling(max_min):
            feeling = ['great','ok','bad','horrible']
            feeling_great=range(0,6)
            feeling_ok=range(6,11)
            feeling_bad=range(11,46)
            if max_min in feeling_great:
                return feeling[0]
            elif max_min in feeling_ok:
                return feeling[1]
            elif max_min in feeling_bad:
                return feeling[2]
            else:
                return feeling[3]

        def get_random_feeling_url(feeling):
            url = random.choice(self.fb_gifs[feeling])
            return url

        def fb_gif(url, message):
            post = {'message': '%s' %(message), 'description': '%s' %(message),'link':str(url)}
            facebook_post = requests.post(self.fb_url, data=post).text

        entry_feeling = get_feeling(entry_max)
        exit_feeling = get_feeling(exit_max)

        if entry_feeling is exit_feeling:
            # Generate 1 fb message for both entry and exit.
            gif_url = get_random_feeling_url(entry_feeling)
            fb_message = 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s deri %s minuta p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb'' dhe %s deri %s minuta p'u'\xeb''r t'u'\xeb'' dalur.\n #Mir'u'\xeb''sevini #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border,str(entry_min), str(entry_max), str(exit_min), str(exit_max))
            # fb
            fb_gif(gif_url, fb_message)
        else:
            # Generate 2 fb messages: one for entry and one for exit.
            gif_url_entry = get_random_feeling_url(entry_feeling)
            gif_url_exit = get_random_feeling_url(exit_feeling)

            fb_message_entry = 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s deri %s minuta p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb''. #Mir'u'\xeb''sevini' % (border,str(entry_min), str(entry_max))
            fb_message_exit = 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s deri %s minuta p'u'\xeb''r t'u'\xeb''dal'u'\xeb'' nga #Kosova. #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border, str(exit_min), str(exit_max))

            # fb
            fb_gif(gif_url_entry, fb_message_entry)
            fb_gif(gif_url_exit, fb_message_exit)
