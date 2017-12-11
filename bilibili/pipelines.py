# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
import sys
import re

class BilibiliPipeline(object):
    def __init__(self):
        pass

    def open_spider(self,spider):
        if spider.name == "bili":
            self.file_bili = open('bilibili.json', 'wb')
        elif spider.name == "youku":
            self.file_youku = open('youku.json','wb')
        elif spider.name == "qq":
            self.file_qq = open('qq.json', 'wb')
        elif spider.name == "iqiyi":
            self.file_iqiyi = open('iqiyi.json', 'wb')


    def process_item(self, item, spider):
        if spider.name == "bili":
            bili = dict(item)
            timeArray = time.strptime(bili['time'][0]+":00", "%Y-%m-%dT%H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            bili['time']=str(timeStamp)
            bili['title'] = bili['title'][0]
            bili['author'] = bili['author'][0]
            bili['description'] = bili['description'][0]
            #ensure_ascii=false保证汉字不用ascii码来表示
            content = json.dumps(bili, ensure_ascii=False) + "\n"
            self.file_bili.write(content.encode(encoding="utf-8"))
            return item
        elif spider.name == "youku":
            youku = dict(item)
            youku['title'] = youku['title'][0]
            youku['author'] = youku['author'][0]
            youku['link'] = youku['link'][0]
            #补充优酷的link没有协议头
            match = re.match("^http", youku['link'])
            if match is None:
                youku['link'] = 'http:' + youku['link']
            content = json.dumps(youku, ensure_ascii=False) + "\n"
            self.file_youku.write(content.encode(encoding="utf-8"))
            return item
        elif spider.name == "qq":
            qq = dict(item)
            timeArray = time.strptime(qq['time'][0]+"T00:00:00", "%Y-%m-%dT%H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            qq['title'] = qq['title'][0]
            qq['time'] = str(timeStamp)
            qq['link'] = qq['link'][0]
            content = json.dumps(qq, ensure_ascii=False) + "\n"
            #encode(encodeing="utf-8")保证编码是utf-8
            self.file_qq.write(content.encode(encoding="utf-8"))
            return item
        elif spider.name == "iqiyi":
            iqiyi = dict(item)
            timeArray = time.strptime(iqiyi['time'][0]+"T00:00:00", "%Y-%m-%dT%H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            iqiyi['title'] = iqiyi['title'][0]
            iqiyi['time'] = str(timeStamp)
            iqiyi['link'] = iqiyi['link'][0]
            content = json.dumps(iqiyi, ensure_ascii=False) + "\n"
            self.file_iqiyi.write(content.encode(encoding="utf-8"))
            return item


    def close_spider(self, spider):
        if spider.name == "bili":
            self.file_bili.close()
        elif spider.name == "youku":
            self.file_youku.close()
        elif spider.name == "qq":
            self.file_qq.close()
        elif spider.name == "iqiyi":
            self.file_iqiyi.close()