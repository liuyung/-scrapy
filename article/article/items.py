# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#指定字段
import scrapy


'''class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass'''

class jobboleaticleitem(scrapy.Item):
    #字段来自于jobbole.py里面的变量（需要保存的变量）
    bookname=scrapy.Field() #只能有Field数据类型
    bookauthor=scrapy.Field()
    type=scrapy.Field()
    bookurl=scrapy.Field()
