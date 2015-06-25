#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['URL'] in self.ids_seen:
            raise DropItem("Duplicate item found: %S" % item)
        else:
            self.ids_seen.add(item['URL'])
            return item


class NewsPoolPipeline(object):
    insert_sql = """insert into fx_news(%s) values(%s)"""
    def __init__(self):
        dbargs = settings.get('DB_CONNECT')
        db_server = settings.get('DB_SERVER')
        self.dbpool = adbapi.ConnectionPool(db_server, **dbargs)

    def __del__(self):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.insert_data(item, self.insert_sql)
        return item

    def insert_data(self, item, insert_sql):
        keys = item.fields.keys()
        fields = ','.join(keys)
        qm = ','.join(['%s'] * len(keys))
        sql = insert_sql % (fields, qm)
        data = [item[k] for k in keys]
        return self.dbpool.runOperation(sql, data)



