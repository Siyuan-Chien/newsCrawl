#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from newsCrawl.items import NewscrawlItem
from classifier_wordFre import classifier
from dictionary import kinds_flag
import time

class FxSpider(CrawlSpider):
    name = 'FxSpider'
    allowed_domains = ['news.fx678.com']
    start_urls = [
                  "http://news.fx678.com/",
                  "http://zhibo.fx678.com/",
                  "http://news.fx678.com/news/top/index.shtml",
                  "http://www.fx678.com/News/CentralBank/FED.html",
                  "http://news.fx678.com/news/bank/index.shtml",
                  "http://news.fx678.com/news/usa/index.shtml",
                  "http://news.fx678.com/news/china/index.shtml",
                  "http://news.fx678.com/news/europe/index.shtml",
                  "http://news.fx678.com/news/america/index.shtml",
                  "http://news.fx678.com/news/asia/index.shtml",
                  "http://news.fx678.com/news/otherarea/index.shtml"
                 ]
    rules = (
            Rule(SgmlLinkExtractor(allow = ('/C/2015(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])/2015(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{10}')),
                                   callback = 'parse_page', process_request='add_cookie', follow=True),
            )

    def add_cookie(self, request):
        request.replace(cookies = [])
        return request

    def parse_page(self, response):
        self.log('Fetch FxNews page: %s' %response.url)
        item = NewscrawlItem()
        item['title'] = response.xpath('/html/body/div[7]/div[1]/div[2]/text()').extract()[0].encode('utf-8')
        item['URL'] = response.url
        time_common = response.xpath('/html/body/div[7]/div[1]/div[3]/span[1]/text()').extract()[0].replace(u'\u5e74',u'-').replace(u'\u6708', u'-').replace(u'\u65e5', '').encode('utf-8')+':00'
        item['time'] = int(time.mktime(time.strptime(time_common, '%Y-%m-%d %H:%M:%S')))
        item['content'] = response.xpath('/html/body/div[7]/div[1]/div[4]/div[1]/p[1]').extract()[0].encode('utf-8')
        item['tags'] = ','.join(response.xpath('/html/body/div[7]/div[1]/div[4]/div[1]/div[2]/div[2]/ul/li/a/text()').extract()).encode('utf-8')
        [item['JPY_news'], item['JPY_norm'], item['JPY_analy'], item['CHF_news'], item['CHF_norm'], item['CHF_analy'],
         item['USD_news'], item['USD_norm'], item['USD_analy'], item['EUR_news'], item['EUR_norm'], item['EUR_analy'],
         item['GBP_news'], item['GBP_norm'], item['GBP_analy'], item['AUD_news'], item['AUD_norm'], item['AUD_analy'],
         item['CAD_news'], item['CAD_norm'], item['CAD_analy'], item['RMB_news'], item['RMB_norm'], item['RMB_analy'],
         item['gold'], item['silver'], item['crude'], item['bond']] = classifier(item['title'],item['tags'], kinds_flag)
        item['importance'] = 0

        return item
