import scrapy
from lianjia.http import MyRequest
from lianjia.items import LianjiaItem


class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    max_page = 20
    id = 1
    start_urls = ["https://bj.fang.lianjia.com/loupan/"]

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url,
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'page': 1})

    def parse(self, response, **kwargs):
        houses = response.xpath("/html/body/div[3]/ul[2]/li")

        for house in houses:
            try:
                print(house)
                item = LianjiaItem()
                item['name'] = house.xpath(
                    "./div/div[1]/a/text()").get().strip()
                locations = house.xpath("./div/div[2]")
                item['location0'] = locations.xpath(
                    "./span[1]/text()").get().strip()
                item['location1'] = locations.xpath(
                    "./span[2]/text()").get().strip()
                item['location2'] = locations.xpath("./a/text()").get().strip()
                item['type'] = house.xpath(
                    "./div/a/span[1]/text()").get().strip()
                item['size'] = int(
                    house.xpath("./div/div[3]/span/text()").get().split(' ')
                    [1].split('-')[0].strip('㎡'))

                flag = house.xpath(
                    "./div/div[6]/div[1]/span[2]/text()").get().strip()
                if flag == '元/㎡(均价)':
                    item['perunit'] = int(
                        house.xpath("./div/div[6]/div[1]/span[1]/text()").get(
                        ).split('-')[0])
                    item['price'] = round(item['perunit'] * item['size'] /
                                          10000)
                    item['perunit'] = round(item['perunit'] / 10000, 4)
                else:
                    print('\n\n\nasdfasdfasdfasdf\n\n')
                    print(flag)
                    item['price'] = int(
                        house.xpath("./div/div[6]/div[1]/span[1]/text()").get(
                        ).split('-')[0])
                    item['perunit'] = round(item['price'] / item['size'], 4)

                self.id += 1
                yield item
            except:
                print('Error occured.')

        if kwargs["page"] + 1 <= self.max_page:
            nxt_page_url = self.start_urls[0] + f'pg{kwargs["page"]+1}'
            yield MyRequest(url=nxt_page_url,
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'page': kwargs["page"] + 1})