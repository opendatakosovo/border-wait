import os, requests
from borderwait import settings

gifs_directory = settings.GIFS_DIRECTORY
WAIT_TIME_GIF_URLS = settings.WAIT_TIME_GIF_URLS
max_gif_size = settings.GIF_MAX_SIZE

feelings = ['great', 'ok', 'bad', 'horrible']
for feels in feelings:
    for url in WAIT_TIME_GIF_URLS[feels]:
        gif_name = url.split('/')[3]
        gif = '%s/%s/%s'% (gifs_directory,feels,gif_name)
        if os.path.isfile(gif):
            print 'gif exitsts: %s' % gif_name
        else:
            request = requests.get(url, stream=True)
            if request.status_code == 200:
                if not os.path.exists(os.path.dirname(gif)):
                    try:
                        print 'creating folder /%s' % feels
                        os.makedirs(os.path.dirname(gif))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(gif, 'wb') as gf:
                    print 'downloading gif %s' % gif_name
                    for chunk in request:
                        gf.write(chunk)
                    # Tweepy allows posting gifs at max size of 3mb, so we check if gif is under 3mb.
                    if os.path.getsize(gif) > max_gif_size:
                        print 'size is too big, deleting file '+ gif_name
                        os.remove(gif)
                    else:
                        print 'size is ok: %s' % os.path.getsize(gif)
