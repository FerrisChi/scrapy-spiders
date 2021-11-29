import scrapy
from lianjia.http import MyRequest
from lianjia.items import LianjiaItem

class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    max_page = 1
    id = 1
    start_urls = [
        "https://bj.lianjia.com/ershoufang/xicheng/",
        "https://bj.lianjia.com/ershoufang/dongcheng/",
        "https://bj.lianjia.com/ershoufang/haidian/",
        "https://bj.lianjia.com/ershoufang/chaoyang/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url,
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'page': 1})

    def parse(self, response, **kwargs):
        houses = response.xpath("/html/body/div[4]/div[1]/ul/li")

        for house in houses:
            item = LianjiaItem()
            item['name'] = house.xpath("./div[1]/div[1]/a/text()").get()
            price = house.xpath("./div[1]/div[6]/div[1]/span/text()").get(
            ) + house.xpath("./div[1]/div[6]/div[1]/i[last()]/text()").get()
            item['price'] = price
            item['size'] = house.xpath(
                "./div[1]/div[3]/div/text()").get().split('|')[1].strip()
            item['perunit'] = house.xpath(
                "./div[1]/div[6]/div[2]/span/text()").get()
            item['region'] = response.url.split('/')[4]
            item['id'] = self.id
            self.id += 1
            yield item

        if kwargs["page"] + 1 < self.max_page:
            nxt_page_url = response.xpath(
                "/html/body/div[4]/div[1]/div[7]/div[2]/div/a[last()]/@href"
            ).get()
            yield MyRequest(url=response.urljoin(nxt_page_url),
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'page': kwargs["page"] + 1})
