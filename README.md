# Border Wait - Crawler and Bot Application

Border Wait is a python web crawler, facebook and twitter bot - crawls the data from [Qendra Kombëtare për Menaxhim Kufitar (QKMK)](https://mpb.rks-gov.net/QKMK.aspx) then posts and tweets the delays at each border with a specifc gif on facebook and twitter.

## Technologies
* Operating System: **[Ubuntu 14.04 LTS](https://www.ubuntu.com/)**
* Language: **[Python](https://www.python.org/)**
* Crawling Framework: **[Scrapy](http://scrapy.readthedocs.io/en/latest/)**
* Scrapy Deploy and Control Spider API: **[Scrapyd](http://scrapyd.readthedocs.io/en/latest/)**
* Python Twitter API: **[Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/)**
* Database: **[MongoDB](https://www.mongodb.com/)**
* MongoDB ORM: **[PyMongo](https://api.mongodb.com/python/current/)**
* Web Server: **[NGINX](https://www.nginx.com/)**

## Setup and installing prerequisites
GPG (GNU Privacy Guard) is the tool used in secure apt to sign files and check their signatures.

apt-key is a program that is used to manage a keyring of gpg keys for secure apt. The keyring is kept in the file /etc/apt/trusted.gpg (not to be confused with the related but not very interesting  /etc/apt/trustdb.gpg). apt-key can be used to show the keys in the keyring, and to add or remove a key.

**NOTE!!!** These packages are currently not updated and may not work on Ubuntu 16.04 or later versions.

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

Install Git:
```
sudo apt-get install git
```

Go inside the projects folder and install scrapyd using pip:
```
sudo pip install -e git+https://github.com/scrapy/scrapyd.git@32be9b85b0ba496e5a5d983ee492f1116f9cfbb9#egg=scrapyd
```

**NOTE!!!** In order to avoid some errors, you have to downgrade the Twisted package to version 16.4.1:
```
sudo pip install Twisted==16.4.1
```

Install dependencies:
```
sudo pip install pyasn1 tweepy --upgrade
```

## Preparing the project

Clone the project in your machine:
```
git clone https://github.com/opendatakosovo/border-wait.git
cd border-wait
```

Adding the Facebook and Twitter API Access Tokens:
```
cd borderwait
sudo nano settings.py

...
# TWITTER ACCESS TOKENS FOR TWITTER BOT
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# FACEBOOK ACCESS TOKENS FOR FACEBOOK BOT
FACEBOOK_ACCESS_TOKEN = ''
...
```

Get global root project path (use pwd command in root project path to get the global path):
```
pwd
/home/<user>/border-wait
```

Set the global root project path into settings.py
```
cd borderwait
sudo nano settings.py

...
GLOBAL_PROJECT_DIRECTORY = '/home/<user>/border-wait'
...
```

## Deploying the project

### Installing prerequisites

Install nginx for the reverse proxy and apache2-utils for the login security:
```
sudo apt-get install nginx apache2-utils
```

Now create a user and password:
```
sudo htpasswd -c /etc/nginx/.htpasswd <type your username>
```

Hit enter and will ask you for a password.
Then you need to edit the configurations file of nginx to create a reverse proxy to the scrapyd webservice.
```
sudo nano /etc/nginx/sites-available/default
```

then edit the config file according to this:
```
server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        root /usr/share/nginx/html;

        # Make site accessible from http://localhost/
        server_name _;
        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        location ~ /\.ht {
                deny all;
        }

        location / {
                proxy_pass http://localhost:6800;
                auth_basic "Restricted Content";
                auth_basic_user_file /etc/nginx/.htpasswd;
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                #try_files $uri $uri/ =404;
        }
}

```
now reload nginx service:
```
sudo service nginx reload
```

### Securing Scrapyd service
First of all you need to block scrapyd to be accessed by outside the server. To do this you have to edit the scrapyd configuration file:
```
sudo nano /etc/scrapyd/conf.d/000-default
```

then add a bind address above the port and set it to 127.0.0.1(default is set to 0.0.0.0):
```
bind_address = 127.0.0.1
```

the restart scrapyd service:
```
sudo service scrapyd restart
```

### Deploy the project
Go inside the project's folder and run the command below to deploy the project:
```
scrapyd-deploy -p borderwait
```
**Note:** If you have errors when running command above please remove folder **project.egg-info** and **build** inside project folder.

If you want to delete deployed project:
```
curl http://localhost:6800/delproject.json -d project=borderwait
```

#### Running the spiders
Scrapyd can be accessed by outside since it uses the localhost(0.0.0.0), so we need to block it by changing the localhost to 127.0.0.1 which blocks outside world from entering.
```
curl http://localhost:6800/schedule.json -d project=borderwait -d spider=borderwait
```


## Authors

* **[Georges Labrèche](https://github.com/georgeslabreche)** & **[Diamant Haxhimusa](https://github.com/diamanthaxhimusa)** & **[Arianit Hetemi](https://github.com/arianithetemi)**
