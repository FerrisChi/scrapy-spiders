# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WrdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    confirmedcases = scrapy.Field()


class Wrdata2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    confirmedcases_ratio = scrapy.Field()

class Wrdata3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    confirmedcases_perday = scrapy.Field()

class Wrdata4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    confirmeddeath = scrapy.Field()

class Wrdata5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    vaccinated = scrapy.Field()

class Wrdata6Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    day = scrapy.Field()
    confirmeddeath_ratio = scrapy.Field()
