# -*- coding: utf-8 -*-
import scrapy
from ..tools.starturl import starturl


class IqiyiSpider(scrapy.Spider):
    name = 'iqiyi'
    allowed_domains = ['iqiyi.com']
    start_urls = starturl.assemblUrl(starturl, name)

    def parse(self, response):
        for sel in response.xpath('//li[@class="list_item"]'):
            item = {}
            # 解出refer，header是个list，list中的每一项是经过bytes编码的
            keyword = starturl.parseUrl(self, response.url, self.name)
            uid = starturl.hammal_uids[keyword]
            item['uid'] = uid
            item['source'] = "iqiyi"
            item['title'] = sel.xpath('a/img/@title').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['time'] = sel.xpath('div[@class="result_info result_info-180101"]/div[@class="info_item"]/div[@class="result_info_cont result_info_cont-half"]/em[@class="result_info_desc"]/text()').extract()
            yield item



if __name__ == '__main__':
    url = starturl.assemblUrl(starturl, 'iqiyi')
    print (url)
