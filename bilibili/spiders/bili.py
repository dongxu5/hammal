# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..tools.starturl import starturl
import sys

class BiliSpider(CrawlSpider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = []
    # for i in range(2):
    #      start_urls.append('https://search.bilibili.com/video?keyword=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&page='+str(i+1)+'&order=pubdate&duration=1')
    start_urls = starturl.assemblUrl(starturl, name)
    rules = (
        Rule(LinkExtractor(allow=r'/av\d{8}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['link'] = response.url
        i['title'] = response.xpath('//div[@class="info"]/div[@class="v-title"]/h1/text()').extract()
        i['time'] = response.xpath('//time[@itemprop="startDate"]/@datetime').extract()
        i['author'] = response.xpath('//div[@class="upinfo"]/div[@class="r-info"]/div[@class="usname"]/a[@class="name"]/text()').extract()
        i['description'] = response.xpath('//div[@class="v_info"]/div[@class="intro"]/div[@id="v_desc"]/text()').extract()
        i['source'] = "bilibili"
        i['uid'] = "1234"
        return i

if __name__ == '__main__':
    url = starturl.assemblUrl(starturl, 'bili')
    print (url)