import pymongo, datetime
from scrapy.exceptions import DropItem

# Save the item in MongoDB
class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB', 'items'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        dbs = self.client.database_names()
        #IF DB IS EMPTY OR NOR CREATED YET CREATE IT AND FILL IT WITH DATA.
        if self.db.name in dbs:
            border = item['border']
            time = item['time']
            # latest_doc is equal to the border name
            latest_doc = self.db[self.mongo_collection].find_one({"border.border": border})
            # here we check if the the border name exists on the database, if not we save it
            if latest_doc:
                # here we set the laatest doc to the last saved doc by that border name
                latest_doc = self.db[self.mongo_collection].find({"border.border": border}).sort("timestamp", -1).limit(1)
                for value in latest_doc:
                    # here we check if the time the gov. updated the delays is equal to the last saved time from database
                    # AND if name of the border is equal to the latest doc
                    # if yes then we save the border to database and stop the process from going to the next pipeline(stoping social media posting)
                    if time == value['border']['time'] and border == value['border']['border']:
                        self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
                        raise DropItem("Duplicate item found: %s" % item)
                    else:
                        self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
                        return item
            else:
                self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
                return item
        else:
            self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
            return item
