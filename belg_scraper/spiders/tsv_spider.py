
#
# This file is part of https://github.com/AvidSoftware-be/StaatsbladScraper, licensed under GNU Affero GPLv3 or later.
#

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.utils.response import get_base_url
from scrapy.http import FormRequest, Request
import re
from belg_scraper.items import BelgScraperItem
import datetime



class tsvSpider(CrawlSpider):
    name = "tsv"
    allowed_domains = ["www.ejustice.just.fgov.be"]
    
    def __init__(self, postkode='8800',van='1900-01-01',tot='3000-01-01', *args, **kwargs):
        super(tsvSpider, self).__init__(*args, **kwargs)
        self.postkode = postkode
        self.validate(van)
        self.validate(tot)
        self.from_date = van 
        self.to_date = tot
        self.pdda = str(datetime.datetime.strptime(van, '%Y-%m-%d').year)
        self.pddm = str(datetime.datetime.strptime(van, '%Y-%m-%d').month).zfill(2) 
        self.pddj = str(datetime.datetime.strptime(van, '%Y-%m-%d').day).zfill(2) 
        self.pdfa = str(datetime.datetime.strptime(tot, '%Y-%m-%d').year) 
        self.pdfm = str(datetime.datetime.strptime(tot, '%Y-%m-%d').month).zfill(2)
        self.pdfj = str(datetime.datetime.strptime(tot, '%Y-%m-%d').day).zfill(2)
    
    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")


    def start_requests(self):
        return [FormRequest(url="http://www.ejustice.just.fgov.be/cgi_tsv/tsv_rech.pl?language=nl", 
                            formdata={'postkode': str(self.postkode), 'akte':'c01', 'pdda':self.pdda, 'pddm':self.pddm, 'pddj':self.pddj, 'pdfa':self.pdfa, 'pdfm':self.pdfm, 'pdfj':self.pdfj},
                            callback=self.parseCount)]

    def parseCount(self,response):
        m = re.search('\>\s&nbsp;&nbsp;&nbsp;(\d+)\n\<', response.body)
        count = m.group(1)

        #Generate URL's
        base_url = "http://www.ejustice.just.fgov.be/cgi_tsv/tsv_l_1.pl?lang=nl&sql=postkode+contains+%27" + \
                   self.postkode +"%27+and+pd+between+date%27" + self.from_date + "%27+and+date%27" + self.to_date + \
                   "%27++and+akte+contains+%27c01%27&fromtab=TSV&pdda=" + self.pdda + "&pddm=" + self.pddm + \
                   "&pddj=" + self.pddj + "&pdfa=" + self.pdfa + "&pdfm=" + self.pdfm + "&pdfj=" + self.pdfj + "&postkode=" + self.postkode + "&akte=c01"

        url_list = []
        for x in range(0,int(count),30):
            url_list += [base_url + "&row_id=" + str(x+1)]
        
        requests = []
        requests += [scrapy.Request(x, self.parseItems) for x in url_list]
        return requests

    def parseItems(self,response):
        for sel in response.xpath('//table/tr[*]/td[2]'):
            item = BelgScraperItem()
            item['name'] = sel.xpath('.//text()').extract()[1] + sel.xpath('.//text()').extract()[2]
            item['address'] = sel.xpath('.//text()').extract()[3]
            item['zipcode'] = sel.xpath('.//text()').extract()[3]
            item['city'] = sel.xpath('.//text()').extract()[3]
            item['number'] = sel.xpath('.//text()').extract()[4]
            item['date'] = sel.xpath('.//text()').extract()[6] + sel.xpath('.//text()').extract()[7]
            print(item['date'])
            yield item
        return
