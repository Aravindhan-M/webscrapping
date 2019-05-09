# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
#

import json
import csv

#
# test = "test \\u0643\\uFEBD"
# print(test.encode("utf-8").decode('unicode-escape')) => test كﺽ


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('itemssouqarabic.jl', 'w',encoding = 'utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        print(line)
        self.file.write(line)
        return item


class JsonWriterPipeline2(object):

    def open_spider(self, spider):
        # self.file = open('itemstitle.jl', 'w')
        # self.file = open('itemstest.csv', 'w',encoding = 'utf-8',newline='')
        self.file = open('souq_arabictest.csv', 'w',encoding = 'utf-8',newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item['link'].append("image_path")
        for items in item['images']:
            item['link'].append(items['path'])
        wr = csv.writer(self.file,dialect='excel')
        wr.writerows([item['link']])
        return item


class JsonWriterPipelineAxiom(object):

    def open_spider(self, spider):
        self.file = open('axiomlink.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class JsonWriterPipelineAxiom2(object):

    def open_spider(self, spider):
        self.file = open('axiomextract.csv', 'w',encoding = 'utf-8-sig',newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        wr = csv.writer(self.file,dialect='excel')
        wr.writerows([item['link']])
        return item

# Pipelines for LULU


class JsonWriterPipelineLULU(object):

    def open_spider(self, spider):
        self.file = open('lulu.jl', 'w',encoding = 'utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        print(line)
        self.file.write(line)
        return item


class JsonWriterPipelineLULU2(object):

    def open_spider(self, spider):
        self.file = open('lulucsvtest.csv', 'w',encoding = 'utf-8',newline='')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item['link'].append("image_path")
        for items in item['images']:
            item['link'].append(items['path'])
        wr = csv.writer(self.file,dialect='excel')
        wr.writerows([item['link']])
        return item
