# -*- coding: utf-8 -*-
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
