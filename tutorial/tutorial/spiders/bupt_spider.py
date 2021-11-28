import scrapy
from tutorial.items import BuptItem

import sys
print('bupt_spider.py',sys.path)

class BuptSpider(scrapy.Spider):
    name = "bupt"
    allowed_domains = ["bupt.edu.cn/"]
    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]

    def parse(self, response):
        item = BuptItem()
        s="/html/body/div/div[2]/div[2]/div/ul/li[4]/div/ul/li"
           
        for x in response.xpath(s):
            # x = response.xpath(s + "/li[{%d}]".format(i))
            item['school'] = x.xpath("./a/text()").extract()
            print('school',x.xpath("./a/text()").extract())
            item['link'] = x.xpath("./a/@href").extract()
            print('link:',x.xpath("./a/@href").extract())
            if item['school'] and item['link']:
                yield(item)