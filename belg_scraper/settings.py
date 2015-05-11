# -*- coding: utf-8 -*-

# Scrapy settings for belg_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
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
