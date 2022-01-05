# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import csv


class CovidPipeline:

    header = [
        'id', 'country', 'total_cases', 'new_cases', 'total_deaths',
        'new_deaths', 'total_recovered', 'new_recovered', 'active_cases',
        'serious_critical', 'total_cases', 'deaths', 'total_tests', 'tesets',
        'population'
    ]
    items = []

    def open_spider(self, spider):
        try:
            self.file = open('result.csv', "w", encoding="utf-8", newline='')
        except Exception as err:
            print(err)
        self.f_csv = csv.DictWriter(self.file, self.header)
        self.f_csv.writeheader()

    def process_item(self, item, spider):
        print(item)
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        print(self.items)
        self.f_csv.writerows(self.items)
        self.file.close()