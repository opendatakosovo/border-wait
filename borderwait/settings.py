# -*- coding: utf-8 -*-

# Scrapy settings for borderwait project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'borderwait'

SPIDER_MODULES = ['borderwait.spiders']
NEWSPIDER_MODULE = 'borderwait.spiders'

# MONGODB SETTINGS
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'borderwait' #database name
MONGO_COLLECTION = 'waits' #database collection

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'border (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# TWITTER ACCESS TOKENS FOR TWITTER BOT
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

#FACEBOOK ACCESS TOKENS FOR FACEBOOK BOT
FACEBOOK_ACCESS_TOKEN = ''

WAIT_TIME_GIF_URLS = {
   'great': [
      'http://i.giphy.com/kGMPV3ehtc7aE.gif',
      'http://i.giphy.com/UKm1AF0UrCkb6.gif',
      'http://i.giphy.com/qcMjXuCugvMXK.gif',
      'http://i.giphy.com/A854pmlcoiHni.gif',
      'http://i.giphy.com/cAfaWIcWr7qus.gif',
      'http://i.giphy.com/mIMsLsQTJzAn6.gif',
      'http://i.giphy.com/CAxbo8KC2A0y4.gif',
      'http://i.giphy.com/qCYJu1d0VfJTy.gif',
      'http://i.giphy.com/3otPoHqjMbo6JJ1FMk.gif',
      'http://i.giphy.com/UjSdO0uoyGeac.gif',
      'http://i.giphy.com/UiJ8YgFH2hlC.gif'
   ],
   'ok': [
      'http://i.giphy.com/3o7TKCGuEkIrLZ0E2Q.gif',
      'http://i.giphy.com/cPngiJPGKsfUQ.gif',
      'http://i.giphy.com/g790a3PzUHbs4.gif',
      'http://i.giphy.com/RIymi3HoG8jNS.gif',
      'http://i.giphy.com/QZbB48rGqylYk.gif',
      'http://i.giphy.com/xT0BKBY1YIfxxtk092.gif',
      'http://i.giphy.com/11fucLQCTOdvBS.gif',
      'http://i.giphy.com/pFkbkttdEBnSo.gif',
      'http://i.giphy.com/g0MQ2Pyi5Z3s4.gif',
      'http://i.giphy.com/9B5DEBbKQwwQE.gif'
   ],
   'bad': [
      'http://i.giphy.com/xTiTniwPRUeB59PNQc.gif',
      'http://i.giphy.com/bP2bOuWDpVM7C.gif',
      'http://i.giphy.com/NN5cAmTFRxpE4.gif',
      'http://i.giphy.com/rEKMO9OWtXjZS.gif',
      'http://i.giphy.com/3o6EhXIhX0HUX5nrsk.gif',
      'http://i.giphy.com/br7gVfL2SRdJK.gif',
   ],
   'horrible': [
      'http://i.giphy.com/59KddieNEF2GQ.gif',
      'http://i.giphy.com/3o7TKFdhXnKtxbn6wg.gif',
      'http://i.giphy.com/nAezPM5bCcuYw.gif',
      'http://i.giphy.com/3o7qE3a5YpLpCdeq0U.gif',
      'http://i.giphy.com/4n9lYreyEcn3a.gif',
      'http://i.giphy.com/4jCxItUVMfHig.gif',
      'http://i.giphy.com/nEL6rKDWEonGU.gif',
      'http://i.giphy.com/xT5LMFVIKfCsH0rkoo.gif',
      'http://i.giphy.com/l46CmHfsiZhKSERxe.gif',
      'http://i.giphy.com/REPi7Zrx4xf5S.gif'
   ]
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'border.middlewares.BorderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'border.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'borderwait.pipelines.mongo.MongoPipeline':100,
    'borderwait.pipelines.twitter.TwitterPipeline':300,
    'borderwait.pipelines.facebook.FacebookPipeline':600
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
