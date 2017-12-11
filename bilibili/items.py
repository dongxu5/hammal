# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    source = scrapy.Field()
    uid = scrapy.Field()
    keyword = scrapy.Field()