from scrapy.exceptions import DropItem
import pymongo, json, datetime, pymongo
from bson import ObjectId

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
        border = item['border']
        time = item['time']
        latestDoc = self.db[self.mongo_collection].find({"border.border": border}).sort("timestamp", -1).limit(1)
        for value in latestDoc:
            if time == value['border']['time'] and border == value['border']['border']:
                self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.db[self.mongo_collection].insert(dict({"timestamp" : datetime.datetime.now() , "border": item }))
                return item
