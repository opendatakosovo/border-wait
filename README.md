# border-wait

BorderWait project is a python web crawler, which crawl the data from [Qendra Kombëtare për Menaxhim Kufitar (QKMK)](mpb-ks.org/qkmk/) and posts the delays of each border with a gif on facebook and twitter.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

* [Ubuntu 14.04 LTS](https://www.ubuntu.com/)
* [Scrapy](http://scrapy.readthedocs.io/en/latest/) - The python web crawling framework.
* [Scrapyd](http://scrapyd.readthedocs.io/en/latest/) - Scrapyd is an application for deploying and running Scrapy spiders.
* [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/) - The python library for accessing the Twitter API.
* [MongoDB & Pymongo](https://www.mongodb.com/) - Nosql open-source databse & Pymongo a python distribution that contains tools for working with MongoDB.

## Installing

##### Ubuntu packages

These packages are currently not updated and may not work on Ubuntu 16.04 and above.


Import the GPG key used to sign Scrapy packages into APT keyring:
```
sudapt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
```
Create /etc/apt/sources.list.d/scrapy.list file using the following command:
```
echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
```
##### Installing Scrapy & Scrapyd
Update package lists and install the scrapy package:
```
sudo apt-get update && sudo apt-get install scrapy
```

Scrapyd-deploy for deploying the scrapy project:

```
sudo apt-get install scrapyd-deploy
```

Go inside the projects folder and install the python scrapyd inside the package:
```
sudo pip install -e git+https://github.com/scrapy/scrapyd.git#egg=scrapyd
```

## Deploying the project

```
scrapyd-deploy -p borderwait
```

### Running the spiders

```
curl http://localhost:6800/schedule.json -d project=borderwait -d spider=borderwait
```

## Authors

* **Georges Labrèche** & **Diamant Haxhimusa**
