# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sqlite3

class DbLink(object):
    databasePath = '/database/ttsFond.db'
    def GetDbConnect(self):
        return sqlite3.connect(self.databasePath)

class DataProvider(object):
    child = None

    def __init__(self, child):
        print('data provider is initialized')
        self.child = child

    def GetCreateTableSql(self):
        if isinstance(self.child, DataProvider):
            print('c is a instance of DataProvider')
            print(dir(self.child))


class TestscrapyItem(DataProvider,scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

    def __init__(self):
        super(TestscrapyItem, self).__init__(self)
        print('item init')
