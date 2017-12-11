#!/bin/bash
export LANG=en_US.UTF-8
cd /data1/www/htdocs/star.hammal.spider.com/bilibili
/usr/local/bin/scrapy crawlall >> /tmp/star_video.log
/usr/bin/python /data1/www/htdocs/star.hammal.spider.com/vdus/main.py >> /tmp/star_video.log
cd ..
rm -f *.json