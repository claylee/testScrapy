# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os
import urllib
import uuid
import os.path
from database import db_session
from models import category
from models import scItems

from scrapy.exceptions import DropItem

class categoryItemPipeline(object):
    def process_item(self,item, spider):
        pass

class TestscrapyPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def serailItem2(self, item):
        urllib.urlretrieve(item["link"],'picture\\'+item["title"])
        print(item['link']," .... down")
        return item

        #cx = sqlite3.connect("picture/test.db")
        #cu.execute("create table imgItems (id integer primary key,pid integer,title varchar(1000) UNIQUE,linkUrl text NULL)")

    def process_item(self, item, spider):
        print('process_item')
        #item.GetCreateTableSql()
        if item is scItems.cateItem:
            cate = piccategory()
            cate.pictitle = item.pictitle
            cate.picurl = item.picurl
            cate.categoryno = item.categoryno
            cate.categoryname = item.categoryname
            cate.categoryurl = item.categoryurl
            cate.tags = item.tags
            db_session.add(cate)
            db_session.commit()
        return

        if item['title'] in self.ids_seen:
            print( "test pipline drop : ", item["title"])
            raise DropItem("Duplicate item found: %s" % item["title"])
        else:
            self.ids_seen.add(item['title'])
            self.serailItem2(item)
            return item

        if path.exists("picture/test.db"):
            print( "test pipline 1 : ", item["title"])
            cx = sqlite3.connect("picture/test.db")
            cx.excute("select count(*) from imgItems where title like ?", item["title"])
            icnt = cx.fetchone()
            if item['title'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
                print( "test pipline drop : ", item["title"])
            else:
                self.ids_seen.add(item['title'])
                print( "test pipline return : ", item["title"])

                self.serailItem2(item)
                return item
        else:
            print( "test pipline 221 : ", item["title"])
            self.serailItem2(item)
            return item

        return item


class SerialPipeline(object):
    def process_item(self, item, spider):
        print( "test pipline 22 : ", item["title"])
        #urllib.urlretrieve(response.urljoin(item["title"]),'picture\\'+item["title"])
        #cx = sqlite3.connect("picture/test.db")
        #cu.execute("create table imgItems (id integer primary key,pid integer,title varchar(1000) UNIQUE,linkUrl text NULL)")
        return item
