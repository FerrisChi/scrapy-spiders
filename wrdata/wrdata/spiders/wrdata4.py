from math import exp
from random import expovariate
import scrapy
from selenium import webdriver
import selenium
from wrdata.http import MyRequest
from wrdata.items import Wrdata4Item


class wrdata4Spider(scrapy.Spider):
    name = "wrdata4"
    start_urls = [
        "https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&zoomToSelection=true&time=2021-12-09&facet=none&uniformYAxis=0&pickerSort=desc&pickerMetric=total_vaccinations_per_hundred&Metric=Confirmed+deaths&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&country=USA~GBR~ISR~DEU~ARE~ARG~FRA"
    ]
    till_day = 23
    avoid = [
        "World", "High income", "Upper middle income", "Asia", "Europe",
        "Lower middle income", "North America", "European Union",
        "South America", "Africa", "Ocean ia", "International"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url,
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'day': 9})

    def parse(self, response, **kwargs):
        lines = response.xpath(
            '/html/body/main/div/div[3]/div/div[1]/div/table/tbody/tr')
        cnt = 0
        for line in lines:
            try:
                item = Wrdata4Item()
                item['country'] = line.xpath('./td[1]/text()').get()
                if item['country'] in self.avoid:
                    continue
                item['day'] = kwargs["day"]
                item['confirmeddeath'] = line.xpath('./td[2]/text()').get()
                if item['confirmeddeath'].find('million') != -1:
                    item['confirmeddeath'] = item['confirmeddeath'].replace(
                        ' million', '')
                    item['confirmeddeath'] = int(
                        float(item['confirmeddeath']) * 1000000)
                else:
                    item['confirmeddeath'] = int(
                        item['confirmeddeath'].replace(',', ''))

                cnt += 1
                yield item
            except:
                print('Error occured.')

        if kwargs["day"] + 1 <= self.till_day:
            nxtday = kwargs["day"]+1
            nxt_page_url = f'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&zoomToSelection=true&time=2021-12-{nxtday}&facet=none&uniformYAxis=0&pickerSort=desc&pickerMetric=total_vaccinations_per_hundred&Metric=Confirmed+deaths&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&country=USA~GBR~ISR~DEU~ARE~ARG~FRA'
            yield MyRequest(url=nxt_page_url,
                            callback=self.parse,
                            dont_filter=True,
                            cb_kwargs={'day': kwargs['day'] + 1})