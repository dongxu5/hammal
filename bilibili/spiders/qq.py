# -*- coding: utf-8 -*-
import scrapy
from ..tools.starturl import starturl
import urllib.parse


class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['v.qq.com']
    start_urls = starturl.assemblUrl(starturl, name)
    def parse(self, response):
        for sel in response.xpath('//div[@class="result_item result_item_h _quickopen"]'):
            item = {}
            keyword = starturl.parseUrl(self, response.url, self.name)
            uid = starturl.hammal_uids[keyword]
            item['uid'] = uid
            item['source'] = "qq"
            item['title'] = sel.xpath('a/img/@alt').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['time'] = sel.xpath('div[@class="result_info"]/div[@class="info_line"]/div[@class="info_item info_item_odd"]/span[@class="content"]/text()').extract()
            yield item
