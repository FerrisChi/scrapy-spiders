# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    country = scrapy.Field()
    total_cases = scrapy.Field()
    new_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    new_deaths = scrapy.Field()
    total_recovered = scrapy.Field()
    new_recovered = scrapy.Field() 
    active_cases = scrapy.Field()
    serious_critical = scrapy.Field()
    total_cases_per_1M = scrapy.Field() 
    deaths = scrapy.Field() 
    total_tests = scrapy.Field() 
    tesets = scrapy.Field()
    population = scrapy.Field()
