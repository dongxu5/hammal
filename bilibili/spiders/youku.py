# -*- coding: utf-8 -*-
import scrapy
from ..tools.starturl import starturl



class YoukuSpider(scrapy.Spider):
    name = "youku"
    allowed_domains = ["www.soku.com"]
    start_urls = starturl.assemblUrl(starturl, name)

    def parse(self, response):
        for sel in response.xpath('//div[@class="v-meta va"]'):
            item = {}
            keyword = starturl.parseUrl(self, response.url, self.name)
            uid = starturl.hammal_uids[keyword]
            item['uid'] = uid
            item['source'] = "youku"
            item['title'] = sel.xpath('div[@class="v-meta-title"]/a/@title').extract()
            item['link'] = sel.xpath('div[@class="v-meta-title"]/a/@href').extract()
            item['author'] = sel.xpath('div[@class="v-meta-entry"]/div[@class="v-meta-data"]/span[@class="username"]/a/text()').extract()
            yield item

