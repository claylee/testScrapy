import scrapy

class cateItem(scrapy.Item):
    pcateid = scrapy.Field()
    title = scrapy.Field()
    picurl = scrapy.Field()
    text = scrapy.Field()
    categoryno = scrapy.Field()
    categoryname = scrapy.Field()
    categoryurl = scrapy.Field()
    tags = scrapy.Field()

class docItem(scrapy.Item):
    pdocid = scrapy.Field()
    pcateid = scrapy.Field()
    title = scrapy.Field()
    docno = scrapy.Field()
    docname = scrapy.Field()
    docpath = scrapy.Field()
    tags = scrapy.Field()


class fileItem(scrapy.Item):
    pdocid = scrapy.Field()
    fileno = scrapy.Field()
    pictitle = scrapy.Field()
    md5code = scrapy.Field()
    picurl = scrapy.Field()
    fpath = scrapy.Field()
    tags = scrapy.Field()
