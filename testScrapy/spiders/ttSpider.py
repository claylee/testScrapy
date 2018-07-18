import scrapy
import urllib
import uuid
import socket
from pprint import pprint

import time
import os
import sys
from scrapy.selector import HtmlXPathSelector
from testScrapy.items import TestscrapyItem
from scrapy.http import Request

sys.path.append(os.path.abspath(""))
print(os.path.abspath(""))
from models import scItems
from models import category,document,picfile
from database import db_session

cateItem = scItems.cateItem
docItem = scItems.docItem
fileItem = scItems.fileItem
piccategory = category.piccategory
picdocument = document.picdocument

class ttSpider(scrapy.Spider):

    def __init__(self):
        self.urlBeen = set()
        self.cateurls = self.getCateUrls()
        self.docurls = self.getDocUrls()

    cateurls = []
    docurls = []
    fileurls = []

    name = "tts"
    allowed_domains = ["http://situiba.com/1009/",
                       "http://situiba.com/"
    ]
    destination = ""
    urlBeen = set()
    download_delay = 1
    timeout = 30
    start_urls = [
        #"http://situiba.com/1009/201611/78900.shtml",
        #"http://situiba.com/1009/list_1296_11.shtml",
        #"http://situiba.com/1009/201705/80153_2.shtml",
        #"http://situiba.com/1009/201705/80163_5.shtml",
        #"http://situiba.com/1009/201610/78730_5.shtml",
        #"http://situiba.com/1009/201301/67240.shtml",
		#"http://situiba.com/1009/201307/69000.shtml",
        "http://situiba.com/1009/list_1296_54.shtml"
    ]

    def parseCategory(self, response):
        hxs = HtmlXPathSelector(response)
        socket.setdefaulttimeout(self.timeout)
        urls = response.xpath('//a/@href').extract()
        print("$$ start cateparse")
        divSelects = response.xpath("//div[@id='body']/div")
        itemlist=[]
        for i in range(6):
            div = divSelects[i]
            #pprint(div.extract())
            alinks = div.xpath("a")
            print("--------------------------")
            print(len(alinks))
            print("--------------------------")
            for a in div.xpath("a"):
                print(a.extract())
                item = cateItem()
                item["picurl"] = a.xpath("@href").extract()[0]
                item["title"] = a.xpath("font/text()").extract()[0]
                item["categoryurl"] = "http://situiba.com" + a.xpath("@href").extract()[0]
                item["categoryname"] = a.xpath("font/text()").extract()[0]
                print(item["picurl"])
                print(item["categoryurl"])
                print(item["categoryname"])
                item["categoryno"] = a.xpath("@href").extract()[0]
                item["tags"] = ""
                itemlist.append(item)
                #yield item
        return itemlist

    def parseDocument(self, response):
        hxs = HtmlXPathSelector(response)
        socket.setdefaulttimeout(self.timeout)
        urls = response.xpath('//a/@href').extract()
        print("$$ start cateparse")
        divSelects = response.xpath("//div[@id='body']/div")
        itemlist=[]
        for i in range(6):
            div = divSelects[i]
            #pprint(div.extract())
            alinks = div.xpath("a")
            print("--------------------------")
            print(len(alinks))
            print("--------------------------")
            for a in div.xpath("a"):
                print(a.extract())
                item = cateItem()
                item["picurl"] = a.xpath("@href").extract()[0]
                item["title"] = a.xpath("font/text()").extract()[0]
                item["categoryurl"] = "http://situiba.com" + a.xpath("@href").extract()[0]
                item["categoryname"] = a.xpath("font/text()").extract()[0]
                print(item["picurl"])
                print(item["categoryurl"])
                print(item["categoryname"])
                item["categoryno"] = a.xpath("@href").extract()[0]
                item["tags"] = ""
                itemlist.append(item)
                #yield item
        return itemlist

    def dowloadImage(self,response):
        for sel in response.xpath('//img[@src]'):
            #fname = str(time.time()) + "_" + str(uuid.uuid1())
            item = TestscrapyItem()
            print('item created')
            imgSrc = sel.xpath('@src').extract()

            iKey = imgSrc[0].strip().replace('/','_')
            if 'litimg' in iKey:
                #print 'not download little image :', iKey
                continue
            #imgSrc = response.urljoin(imgSrc.extract())

            if iKey not in self.urlBeen:
                self.urlBeen.add(iKey)
                item['title'] = iKey
                item['link'] = response.urljoin(imgSrc[0].strip())
                item['desc'] = sel.xpath('@alt').extract()
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                yield item

                relativePath = item['link'].replace("http://situiba.com/","")
                relativePath = relativePath[0:relativePath.rindex('/')]
                relativePath = relativePath.replace("/","\\")
                path = sys.path[0]

                path = os.getcwd() + '\\newPicture\\' + relativePath

                if not os.path.exists(path):
                    os.makedirs(path)

                if not os.path.exists(path + "\\" + item["title"]):
                    try:
                        #os.makedirs(path)
                        print('new one', path + "\\" + item["title"])
                        urllib.urlretrieve(item["link"], path + "\\" + item["title"])
                    except(ExceptionType) as e:
                        print(e)

    def getCateUrls(self):
        urls = []
        for c in db_session.query(piccategory).all():
            urls.append(c)
        return urls

    def getDocUrls(self):
        urls = []
        for c in db_session.query(picdocument).all():
            urls.append(c)
            self.urlBeen.add(c.docpath)
        return urls

    def parse(self, response, dbItem=None):
        hxs = HtmlXPathSelector(response)
        socket.setdefaulttimeout(self.timeout)
        items = []
        icnt = 0
        print("---------------------------------------")
        resDbItem = "no meta"
        if("dbItem" in response.meta):
            resDbItem = response.meta["dbItem"]
        print("resDbItem：",resDbItem)

        if dbItem is None and len(self.cateurls) == 0:
            yield from self.parseCategory(response)
            #return
        elif dbItem is None:
            for cate in self.cateurls:
                print(cate.categoryurl)
                print("each cateurls dbitem is none")
                yield self.make_requests_from_url(cate.categoryurl).replace(callback=lambda response, dbitem=cate: self.parse(response,dbitem))

        if isinstance(dbItem, piccategory):
            sel = response.xpath("//div[@class='lm']")[0]

            #读取分页 urls
            pageurls = sel.xpath(".//ul[contains(@class,'page')]/a/@href").extract()
            for page in pageurls:
                pageurl = response.urljoin(page)
                print(pageurl)
                if(pageurl in self.urlBeen):
                    continue
                print("each page in pageurls, dbitems is cate")
                req = self.make_requests_from_url(pageurl).replace(callback=lambda response, dbitem=dbItem: self.parse(response,dbitem) )

                req.meta["dbItem"] = dbItem
                self.urlBeen.add(pageurl)
                yield req

            #读取每个分页上的document
            docurls = sel.xpath(".//td[contains(@height,'')]")
            for doc in docurls:
                if(len(doc.xpath(".//a/text()").extract())==0):
                    continue
                strurl = doc.xpath(".//a/@href").extract()[0]
                if(strurl in self.urlBeen):
                    continue
                doci = docItem()
                doci["docname"] = doc.xpath(".//a/text()").extract()[0]
                doci["title"] = doc.xpath(".//a/text()").extract()[0]
                doci["docpath"] = doc.xpath(".//a/@href").extract()[0]
                doci["docno"] = ""
                doci["tags"] = doc.xpath(".//a/text()").extract()[0]
                doci["pcateid"] = dbItem.pcateid
                self.urlBeen.add(strurl)
                yield doci

        if dbItem is None:
            for c in self.cateurls:
                print("just print cate urls")
                print(c.title,c.categoryname,c.categoryno,c.categoryurl)
            #yield c
            #yield page

        return

        urls = response.xpath('//a/@href').extract()


        return
        urls = response.xpath('//a/@href').extract()

        validurls = []
        for url in urls:
            url = response.urljoin(url)
            if url not in self.urlBeen:
                #print "**** ... ", url
                self.urlBeen.add(url)
                validurls.append(url)
                #print url

        #for url in validurls:
            #yield Request(url, callback=self.parse)
        items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])
        relPath = 'frake'

        #return items
