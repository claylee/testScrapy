import scrapy

class cateItem(scrapy.Item):

    cateid = scrapy.Field()

    pictitle = scrapy.Field()
    picurl = scrapy.Field()
    categoryno = scrapy.Field()
    categoryname = scrapy.Field()
    categoryurl = scrapy.Field()
    tags = scrapy.Field()
