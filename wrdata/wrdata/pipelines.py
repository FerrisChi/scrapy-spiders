# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


# header = [
#         '2021.12.{}'.format(day) for day in range(9,24)
#     ]
class WrdataPipeline:
    header = [
        'country',
        'day',
        # 'confirmedcases'
        # 'confirmedcases_ratio'
        # 'confirmedcases_perday'
        # 'confirmeddeath'
        # 'vaccinated'
        'confirmeddeath_ratio'
    ]
    items = []

    def open_spider(self, spider):
        try:
            self.file = open('confirmed_death_ratio.csv',
                             "w",
                             encoding="utf-8",
                             newline='')
        except Exception as err:
            print(err)
        self.f_csv = csv.DictWriter(self.file, self.header)
        self.f_csv.writeheader()

    def process_item(self, item, spider):
        # print(item)
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        # print(self.items)
        self.f_csv.writerows(self.items)
        self.file.close()