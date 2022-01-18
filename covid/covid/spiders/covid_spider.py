from math import exp
from random import expovariate
import scrapy
from selenium import webdriver
from covid.http import MyRequest
from covid.items import CovidItem


class covidSpider(scrapy.Spider):
    name = "covid"
    start_urls = ["https://www.worldometers.info/coronavirus/"]

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        # response -- click yesterday
        tableyesterday = response.xpath(
            '/html/body/div[3]/div[3]/div/div[6]/div[2]/div/table')
        # tableyesterday2 = response.xpath(
        #     '/html/body/div[3]/div[3]/div/div[6]/div[3]/div/table')
        thead = tableyesterday.xpath('./thead')
        tbody = tableyesterday.xpath('./tbody[1]')
        # /html/body/div[3]/div[3]/div/div[6]/div[2]/div/table/tbody[3]
        ttail = tableyesterday.xpath('./tbody[3]')

        lines = tbody.xpath('./tr[@class="odd" or @class="even"]')
        cnt = 0
        for line in lines:
            try:
                item = CovidItem()
                item['id'] = int(line.xpath('./td[1]/text()').get())
                try:
                    item['country'] = line.xpath('./td[2]/a/text()').get()
                    if item['country'] == None:
                        item['country'] = line.xpath(
                            './td[2]/span/text()').get()
                except:
                    pass

                try:
                    item['total_cases'] = line.xpath('./td[3]/text()').get()
                    if item['total_cases'] is not None:
                        item['total_cases'] = int(
                            item['total_cases'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['new_cases'] = line.xpath('./td[4]/text()').get()
                    if item['new_cases'] is not None:
                        item['new_cases'] = int(
                            item['new_cases'].strip().strip('+').replace(
                                ',', ''))
                except:
                    pass

                try:
                    item['total_deaths'] = line.xpath('./td[5]/text()').get()
                    if item['total_deaths'] is not None:
                        item['total_deaths'] = int(
                            item['total_deaths'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['new_deaths'] = line.xpath('./td[6]/text()').get()
                    if item['new_deaths'] is not None:
                        item['new_deaths'] = int(
                            item['new_deaths'].strip().strip('+').replace(
                                ',', ''))
                except:
                    pass

                try:
                    item['total_recovered'] = line.xpath(
                        './td[7]/text()').get()
                    if item['total_recovered'] is not None:
                        item['total_recovered'] = int(
                            item['total_recovered'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['new_recovered'] = line.xpath('./td[8]/text()').get()
                    if item['new_recovered'] is not None:
                        item['new_recovered'] = int(
                            item['new_recovered'].strip().strip('+').replace(
                                ',', ''))
                except:
                    pass

                try:
                    item['active_cases'] = line.xpath('./td[9]/text()').get()
                    if item['active_cases'] is not None:
                        item['active_cases'] = int(
                            item['active_cases'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['serious_critical'] = line.xpath(
                        './td[10]/text()').get()
                    if item['serious_critical'] is not None:
                        item['serious_critical'] = int(
                            item['serious_critical'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['total_cases_per_1M'] = line.xpath('./td[11]/text()').get()
                    if item['total_cases_per_1M'] is not None:
                        item['total_cases_per_1M'] = int(
                            item['total_cases_per_1M'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['deaths'] = line.xpath('./td[12]/text()').get()
                    if item['deaths'] is not None:
                        item['deaths'] = int(item['deaths'].strip().replace(
                            ',', ''))
                except:
                    pass

                try:
                    item['total_tests'] = line.xpath('./td[13]/text()').get()
                    if item['total_tests'] is not None:
                        item['total_tests'] = int(
                            item['total_tests'].strip().replace(',', ''))
                except:
                    pass

                try:
                    item['tesets'] = line.xpath('./td[14]/text()').get()
                    if item['tesets'] is not None:
                        item['tesets'] = int(item['tesets'].strip().replace(
                            ',', ''))
                except:
                    pass

                try:
                    item['population'] = line.xpath('./td[15]/a/text()').get()
                    if item['population'] is not None:
                        item['population'] = int(
                            item['population'].strip().replace(',', ''))
                except:
                    pass
                cnt += 1
                yield item
            except:
                print('Error occured.')