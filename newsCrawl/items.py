#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NewscrawlItem(Item):
    URL = Field()
    title = Field()
    time = Field()
    content = Field()
    tags = Field()
    JPY_news  = Field()
    JPY_norm = Field()
    JPY_analy = Field()
    CHF_news = Field()
    CHF_norm = Field()
    CHF_analy = Field()
    USD_news = Field()
    USD_norm = Field()
    USD_analy = Field()
    EUR_news = Field()
    EUR_norm = Field()
    EUR_analy = Field()
    GBP_news = Field()
    GBP_norm = Field()
    GBP_analy = Field()
    AUD_news = Field()
    AUD_norm = Field()
    AUD_analy = Field()
    CAD_news = Field()
    CAD_norm = Field()
    CAD_analy = Field()
    RMB_news = Field()
    RMB_norm = Field()
    RMB_analy = Field()
    gold = Field()
    silver = Field()
    crude = Field()
    bond = Field()
    importance = Field()
