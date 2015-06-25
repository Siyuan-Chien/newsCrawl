#!/usr/bin/python2.7*
#-*- coding:utf-8 -*-

import sys
import jieba

reload(sys)
exec("sys.setdefaultencoding('utf-8')")
assert sys.getdefaultencoding().lower() == "utf-8"

def segment_title(title='我是一只大苹果，又香、又甜、又【好吃】。'):
    exclude = "：；‘’“”！？，。、【】（）%-()/0123456789和将仍对在但或于再".decode('utf-8')
    raw_list = [ch for ch in jieba.cut(title)]
    filter_list = [fil for fil in raw_list if fil not in exclude]
    title_after_segment = ','.join(filter_list).encode('utf-8')
    return title_after_segment

def classifier(title, tags, allKinds):
    string_before_seg = set(segment_title(title+','+tags).split(','))
    flags = []
    for kind in allKinds:
        if (string_before_seg & kind):
            flags.append(1)
        else:
            flags.append(0)
    return flags

if __name__ == '__main__':
    from dictionary import kinds_flag
    """
    kinds_flag = ['JPY_news', 'JPY_norm', 'JPY_analy', 'CHF_news', 'CHF_norm', 'CHF_analy',
                'USD_news', 'USD_norm', 'USD_analy', 'EUR_news', 'EUR_norm', 'EUR_analy',
                'GBP_news', 'GBP_norm', 'GBP_analy', 'AUD_news', 'AUD_norm', 'AUD_analy',
                'CAD_news', 'CAD_norm', 'CAD_analy', 'RMB_news', 'RMB_norm', 'RMB_analy',
                'gold', 'silver', 'crude', 'bond']
    """
    print classifier('中国银行宣布降息，日本央行很激动', '建设银行', kinds_flag)

