# border-wait

BorderWait project is a python web crawler which crawls the data from [Qendra Kombëtare për Menaxhim Kufitar (QKMK)](http://www.mpb-ks.org/qkmk/) and posts the delays at each border with a random gif on facebook and twitter.

### Environment
What things you need to install the software and how to install them.
* [Ubuntu 14.04 LTS](https://www.ubuntu.com/)
* [Scrapy](http://scrapy.readthedocs.io/en/latest/) - The python web crawling framework.
* [Scrapyd](http://scrapyd.readthedocs.io/en/latest/) - Scrapyd is an application for deploying and running Scrapy spiders.
* [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/) - The python library for accessing the Twitter API.
* [MongoDB & Pymongo](https://www.mongodb.com/) - Nosql open-source databse & Pymongo a python distribution that contains tools for working with MongoDB.
* [Nginx](https://www.nginx.com/) - NGINX is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more.

### Initial Setup
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

Go inside the projects folder and install the python scrapyd inside the package:
```
sudo pip install -e git+https://github.com/scrapy/scrapyd.git#egg=scrapyd
```

**NOTE!!!** In order to avoid some errors, you have to downgrade the Twisted package to version 16.4.1:
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

Go inside the project's folder and type:
```
scrapyd-deploy -p borderwait
```

#### Running the spiders
Scrapyd can be accessed by outside since it uses the localhost(0.0.0.0), so we need to block it by changing the localhost to 127.0.0.1 which blocks outside world from entering.
```
curl http://localhost:6800/schedule.json -d project=borderwait -d spider=borderwait
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
sudo service scrapyd stop
sudo service scrapyd start
```

#### Installing prerequisites

Install nginx for the reverse proxy and apache2-utils for the login security:
```
sudo apt-get install nginx apache2-utils
```
Now create a user and password:
```
sudo htpasswd -c /etc/nginx/.htpasswd <type your username>
```
hit enter and will ask you for a password.
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

## Authors

* **[Georges Labrèche](https://github.com/georgeslabreche)** & **[Diamant Haxhimusa](https://github.com/diamanthaxhimusa)**
