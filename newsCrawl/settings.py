#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Scrapy settings for newsCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
SPIDER_MODULES = ['newsCrawl.spiders']
NEWSPIDER_MODULE = 'newsCrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsCrawl (+http://www.yourdomain.com)'

BOT_NAME = 'Mac OS'
USER_AGENT = '%s/%s' % (BOT_NAME, '10_8_3')
DOWNLOAD_DELAY = 1.5
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False
CONCURRENT_ITEMS = 100
ITEM_PIPELINES = {
    'newsCrawl.pipelines.DuplicatesPipeline': 300,
    'newsCrawl.pipelines.NewsPoolPipeline': 800}
DB_SERVER = 'MySQLdb'
DB_CONNECT = {
    'db': 'newsPool',
    'user': 'newSpider',
    'passwd': '123456',
    'host': '127.0.0.1',
    'charset': 'utf8',
    'use_unicode': True}


