#!/usr/bin/python
#
# This file is part of https://github.com/AvidSoftware-be/StaatsbladScraper, licensed under GNU Affero GPLv3 or later.
#

import argparse
import csv
import sys
import argparse
import os

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from belg_scraper.spiders.tsv_spider import tsvSpider
from scrapy.utils.project import get_project_settings

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",
                        help="csv file with postcodes")
    parser.add_argument("-f", "--fromdate", action="store",
                        help="from date/van")
    parser.add_argument("-t", "--todate", action="store",
                        help="to date/tot")
    args = parser.parse_args()

    inputfile = args.inputfile
    d_from = '1900-01-01'
    d_to = '3000-01-01'
    if args.todate:
        d_to = args.todate
    if args.fromdate:
        d_from = args.fromdate

    
   
    
    with open(inputfile, 'rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in lines:
            try:
                int(row[0])
                os.system("scrapy crawl tsv -a postkode={} -a van={} -a tot={}".format(row[0],d_from,d_to))
            except:
                print "Excelp"

if __name__ == "__main__":
    main(sys.argv[1:])
