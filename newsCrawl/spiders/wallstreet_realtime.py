#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

"""
JPY_news,JPY_norm,JPY_analy,CHF_news,CHF_norm,CHF_analy,USD_news,USD_norm,USD_analy,
EUR_news,EUR_norm,EUR_analy,GBP_news,GBP_norm,GBP_analy,AUD_news,AUD_norm,AUD_analy,
CAD_news,CAD_norm,CAD_analy,RMB_news,RMB_norm,RMB_analy,gold,silver,crude,bond,importance
"""

import requests
import json
import MySQLdb
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
from classifier_wordFre import classifier
from dictionary import kinds_flag
import logging

logging.basicConfig()
def scrape():
    page = requests.get('http://api.wallstreetcn.com/v2/livenews')
    news_data = json.loads(page.text)
    total = news_data[u'paginator'][u'total']
    results = news_data[u'results']
    return total, results

def detect(total, TOTAL):
    if total != TOTAL:
        return True
    else:
        return False

def process():
    total, results = scrape()
    file_read = open('./TOTAL', 'rb')
    TOTAL_PREVIOUS = int(file_read.read().strip())
    file_read.close()

    if detect(total, TOTAL_PREVIOUS):
        file_write = open('./TOTAL', 'wb')
        file_write.write(str(total))
        file_write.close()
        conn = MySQLdb.connect(host="localhost",user="newSpider", passwd="123456",
                             db="newsPool", charset='utf8', use_unicode=True)
        cursor = conn.cursor()

        for news in results:
            Time = str(int(time.time()))
            keys_list = ['id','time','title','content',
                        'JPY_news','JPY_norm','JPY_analy','CHF_news','CHF_norm','CHF_analy','USD_news','USD_norm','USD_analy',
                        'EUR_news','EUR_norm','EUR_analy','GBP_news','GBP_norm','GBP_analy','AUD_news','AUD_norm','AUD_analy',
                        'CAD_news','CAD_norm','CAD_analy','RMB_news','RMB_norm','RMB_analy','gold','silver','crude','bond','importance']
            keys = ','.join(keys_list)

            values_str_list_tmp = [news[u'id'], Time, news[u'title'], news[u'contentHtml']]
            value_str_list = ["\""+x.encode('utf-8').replace("\"", "\\\"")+"\"" for x in values_str_list_tmp]
            kinds_list_tmp = classifier(news[u'title'].encode('utf-8'), '', kinds_flag) + [0]
            kinds_list = [str(y) for y in kinds_list_tmp]
            value_list = value_str_list + kinds_list
            values = ','.join(value_list)

            sql = "insert into wallstreet_realtime_news (%s) values(%s)" % (keys, values)
            try:
                cursor.execute(sql)
            except MySQLdb.IntegrityError:
                pass
        cursor.close()
        conn.commit()
        conn.close()
        print "update has been appended"
    else:
        print "there is no update"

def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', seconds=120)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try: # This is here to simulate application activity (which keeps the main thread alive).
        while True: time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() # Not strictly necessary if daemonic mode is enabled but should be done if possible


if __name__ == '__main__':
    process()
    #schedule()
