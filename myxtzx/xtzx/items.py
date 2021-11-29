# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XtzxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    page = scrapy.Field()
    course_name = scrapy.Field()
    teachers = scrapy.Field()
    school = scrapy.Field()
    number = scrapy.Field()
    

