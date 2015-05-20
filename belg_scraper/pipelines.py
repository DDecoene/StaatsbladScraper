# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy import signals
from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter
import csv
import re

class BelgScraperPipeline(object):
    def process_item(self, item, spider):
        #Cleaning of name'
        m = re.search('^(.+)\s(.+),.+\xa0\xa0.+$', item["name"])
        b = re.search('^(.+)\xa0\xa0(.+)$', item["name"])

        if m:
            #print m.group(1)
            item["name"] = m.group(1) + " " + m.group(2)
        elif b:
            #print b.group(1)    
            item["name"] = b.group(1) + " " + b.group(2) 
        
        #Cleaning of address, zip, city
        m = re.search('(\d\d\d\d)\s(.+)\s$',item["city"])
        item["city"]=m.group(2)
        
        m = re.search('(\d\d\d\d)',item["zipcode"])
        item["zipcode"]=m.group(1)

        m = re.search('^\n(.+)\s(\d\d\d\d)\s(.+)\s$',item["address"])

        if m:
            item["address"]=m.group(1)
        else:
            item["address"]=""

        m = re.search('(\d\d\d\d-\d\d-\d\d)',item["date"])
        item["date"] = m.group(1)
        
        m = re.search('^(\d\d\d\.\d\d\d\.\d\d\d).+$',item["number"])
        if m:
            item["number"] = m.group(1)
        else:
            item["number"] = ""

        return item

class CSVPipeline(object):

    def __init__(self):
        self.files = {}
        
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open("{}_{}_{}__{}_{}_{}.csv".format(spider.pdda,spider.pddm,spider.pddj,spider.pdfa,spider.pdfm,spider.pdfj), 'a+b')
        self.files[spider] = file
        kwargs = {}
        kwargs['delimiter'] = ';'
        kwargs['quoting'] = csv.QUOTE_ALL
        self.exporter = CsvItemExporter(file,**kwargs)
        self.exporter.fields_to_export = ["name","address","zipcode","city","number","date"]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
