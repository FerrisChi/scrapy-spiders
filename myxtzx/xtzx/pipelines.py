# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class XtzxPipeline:
    items = []
    header = ['id', 'page', 'course_name', 'teachers', 'school', 'number']

    def open_spider(self, spider):
        try:
            self.file = open('result.csv', "w", encoding="utf-8", newline='')
        except Exception as err:
            print(err)
        self.f_csv = csv.DictWriter(self.file, self.header)
        self.f_csv.writeheader()


    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
    
    def close_spider(self, spider):
        self.f_csv.writerows(self.items)
        self.file.close()
