# -*- coding: utf-8 -*-
#
# This file is part of https://github.com/AvidSoftware-be/StaatsbladScraper, licensed under GNU Affero GPLv3 or later.
#

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BelgScraperItem(scrapy.Item):
# define the fields for your item here like:
    name = scrapy.Field()
    address = scrapy.Field()
    zipcode = scrapy.Field()
    city = scrapy.Field()
    number = scrapy.Field()
    date = scrapy.Field()    
    pass
