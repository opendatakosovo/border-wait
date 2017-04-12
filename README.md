# border-wait

BorderWait project is a python web crawler which crawls the data from [Qendra Kombëtare për Menaxhim Kufitar (QKMK)](mpb-ks.org/qkmk/) and posts the delays at each border with a random gif on facebook and twitter.

### Environment
What things you need to install the software and how to install them.
* [Ubuntu 14.04 LTS](https://www.ubuntu.com/)
* [Scrapy](http://scrapy.readthedocs.io/en/latest/) - The python web crawling framework.
* [Scrapyd](http://scrapyd.readthedocs.io/en/latest/) - Scrapyd is an application for deploying and running Scrapy spiders.
* [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/) - The python library for accessing the Twitter API.
* [MongoDB & Pymongo](https://www.mongodb.com/) - Nosql open-source databse & Pymongo a python distribution that contains tools for working with MongoDB.

### Initial Setup
Ubuntu packages:

These packages are currently not updated and may not work on Ubuntu 16.04 or later versions.

Import the GPG key used to sign Scrapy packages into APT keyring:
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
```
Create /etc/apt/sources.list.d/scrapy.list file using the following command:
```
echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
```
#### Installing Scrapy & Scrapyd
Install these dependecies in order to install Scrapy:
```
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

Update package lists and install the scrapy package:
```
sudo apt-get update && sudo apt-get install scrapy
```
Scrapyd service for deploying and managing spiders:
```
sudo apt-get install scrapyd
```

Scrapyd-deploy for deploying the scrapy project:

```
sudo apt-get install scrapyd-deploy
```

We need to install scrapy python packages as well:
```
sudo pip install scrapy==1.0.5
```

Go inside the projects folder and install the python scrapyd inside the package:
```
sudo pip install -e git+https://github.com/scrapy/scrapyd.git#egg=scrapyd
```

NOTE!!! In order to avoid some errors, you have to downgrade the Twisted package to version 16.4.1:
```
sudo pip install Twisted==16.4.1
```

#### Preparing the project
Getting the project in your local machine:
```
git clone https://github.com/opendatakosovo/border-wait.git
cd border-wait
```
Adding the Facebook and Twitter api tokens:
```
cd borderwait
nano settings.py
.
.
.
# TWITTER ACCESS TOKENS FOR TWITTER BOT
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# FACEBOOK ACCESS TOKENS FOR FACEBOOK BOT
FACEBOOK_ACCESS_TOKEN = ''
```
then add your own Facebook and Twitter api tokens.

###### Donwloading the gifs to post social media:
First we need to set the path where we want to save the gifs.
```
cd borderwait
nano setting.py
.
.
.
# PATH TO SAVE GIFS . DEFAULT IS THE PROJECT DIRECTORY
GIFS_DIRECTORY = './'
```
Then run the downloader.py at project's main folder:
```
python downloader.py
```

#### Deploying the project
```
scrapyd-deploy -p borderwait
```

#### Running the spiders

```
curl http://localhost:6800/schedule.json -d project=borderwait -d spider=borderwait
```

## Authors

* **Georges Labrèche** & **Diamant Haxhimusa**
