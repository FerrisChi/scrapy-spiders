# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XtzxPipeline:
    items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
    
    def close_spider(self, spider):
        try:
            self.file = open('result.json', "w", encoding="utf-8")
        except Exception as err:
            print(err)
        json_str = json.dumps(self.items, ensure_ascii=False, indent=4)
        self.file.write(json_str)
        self.file.close()
