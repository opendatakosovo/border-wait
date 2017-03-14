from scrapy.exceptions import DropItem


# If the new item is the same as the previous one, then ignore/drop it.
class DuplicatesPipeline(object):

    def __init__(self):
        self.previous_item = None

    def process_item(self, item, spider):
        if item is self.previous_item:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.previous_item = item
            return item
