# -*- coding: utf-8 -*-

#
# This file is part of https://github.com/AvidSoftware-be/StaatsbladScraper, licensed under GNU Affero GPLv3 or later.
#

BOT_NAME = 'belg_scraper'

SPIDER_MODULES = ['belg_scraper.spiders']
NEWSPIDER_MODULE = 'belg_scraper.spiders'

ITEM_PIPELINES = {
	#'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
	'belg_scraper.pipelines.BelgScraperPipeline': 300,
	'belg_scraper.pipelines.CSVPipeline': 400,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'belg_scraper (+http://www.yourdomain.com)'
AUTOTHROTTLE_ENABLED = True
