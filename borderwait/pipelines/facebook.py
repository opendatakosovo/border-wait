import requests, random, sys, unicodedata, json
from borderwait import message_generator
reload(sys)
sys.setdefaultencoding('utf-8')

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
        self.fb_videos_url = 'https://graph-video.facebook.com/me/videos?access_token='+self.fb_access_token
        self.fb_post_url = 'https://graph.facebook.com/?access_token='+self.fb_access_token

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

        """
            Getting the feeling value returned from get_feeling definition, and border name,
            will find the right video based on feeling and border name,
            returns the exact path of video in string
        """
        def get_video_feeling_path(feeling, border):
            # Building the path based on border name and feeling
            # filename = border_name + '_' + feeling + '.gif'
            # gif_filename = filename.decode('utf-8')
            # return './%s/%s'%(self.path_to_gifs, feeling, gif_filename)
            return './videos/great/bernjak_great.mp4'

        """ 
            For posting a video in facebook timeline, we need to upload a video
            at our fb account videos, then we need to make another request
            for updating the status of that uploaded video
        """
        def post_video(video_path, message, feeling):
            # Converting the video file into multipart/form-data format
            multipart_video = open(video_path, 'rb')

            # Preparing data content for upload video request
            upload_data = {'file': multipart_video}

            # Making API POST request for uploading this video
            uploaded_video_response = requests.post(self.fb_videos_url, files=upload_data).text

            # Loading as JSON from plain text the response from uploaded video
            json_uploaded_video_response = json.loads(uploaded_video_response)

            """
                To update the status with the actual generated message
                need to make another request to this latest uploaded video post
            """

            # Preparing the data content for updating status
            data = {'id': json_uploaded_video_response['id'],
                    'description': message}

            # Making API POST request to update the status of this video uploaded post
            updated_status_video_post_response = requests.post(self.fb_post_url, data=data).text


        # Getting the feeling based on entry and exit maximum
        entry_feeling = get_feeling(entry_max)
        exit_feeling = get_feeling(exit_max)

        if entry_feeling is exit_feeling:
            # Generate 1 fb message for both entry and exit.
            gif_url = get_video_feeling_path(entry_feeling, border)
            fb_message = message_generator.enter_exit(border, entry_min, entry_max, exit_min, exit_max)
            # fb
            post_video(gif_url, fb_message, entry_feeling)
        else:
            # Generate 2 fb messages: one for entry and one for exit.
            gif_url_entry = get_video_feeling_path(entry_feeling, border)
            gif_url_exit = get_video_feeling_path(exit_feeling, border)

            fb_message_entry = message_generator.enter(border, entry_min, entry_max)
            fb_message_exit = message_generator.exit(border, exit_min, exit_max)

            # fb
            post_video(gif_url_entry, fb_message_entry, entry_feeling)
            post_video(gif_url_exit, fb_message_exit, exit_feeling)
