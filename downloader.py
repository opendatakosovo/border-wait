import os, requests
from borderwait import settings

directory = settings.GIFS_DIRECTORY
WAIT_TIME_GIF_URLS = settings.WAIT_TIME_GIF_URLS

feelings = ['great', 'ok', 'bad', 'horrible']
for feels in feelings:
    for url in WAIT_TIME_GIF_URLS[feels]:
        gif = '%s/%s/%s'% (directory,feels,url.split('/')[3])
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            if not os.path.exists(os.path.dirname(gif)):
                try:
                    os.makedirs(os.path.dirname(gif))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            with open(gif, 'wb') as gf:
                for chunk in request:
                    gf.write(chunk)
