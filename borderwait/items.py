# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BorderWaitItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    time = scrapy.Field()
    border = scrapy.Field()
    entry = scrapy.Field()
    exit = scrapy.Field()
    entry_q = scrapy.Field()
    exit_q = scrapy.Field()
    
    
