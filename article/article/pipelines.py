# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import  ImagesPipeline
import codecs
import json
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import  adbapi  #异步API
#统一处理数据  #item用了存储数据到数据库
'''class ArticlePipeline(object):   #用来保持到数据库等操作
    def process_item(self, item, spider):
        return item
'''
'''class Mysqpipline(object): #采用同步的机制写入MYSQL
    def __init__(self):
      self.conn=MySQLdb.connect('localhost','root','root','novel',charset="utf8",use_unicode=True)
      self.cursor=self.conn.cursor()

    def process_item(self,item,spider):
      sql="insert into quanshu(bookname,bookauthor,`type`,bookurl)  values(%s,%s,%s,%s)"
      self.cursor.execute(sql,(item["bookname"],item["bookauthor"],item["type"],item["bookurl"]))
      self.conn.commit()
      return item'''

class MysqlTwistedPipeline(object):#保存到 Mysql时变为异步（插入未执行完也可以向下继续执行）
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparams)#用**转化成可变化的参数
        return cls(dbpool)
    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常
    def handle_error(self, failure):
        # 处理异步插入异常
        print(failure)
    def do_insert(self,cursor,item):
          sql="insert into quanshu(bookname,bookauthor,`type`,bookurl)  values(%s,%s,%s,%s)"
          cursor.execute(sql,(item["bookname"],item["bookauthor"],item["type"],item["bookurl"]))

'''class jsonpipline(object): #用来导出json文件，自定义的
    def __init__(self):
        self.file=codecs.open("article.json",'w',encoding="utf-8")#打开文件
    def process_item(self, item, spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+" "
        self.file.write(lines)
        return item
    def spider_closwd(self,spider):
        self.file.close()

class articlitempipline(ImagesPipeline):#继承ImagesPipeline，来重新定制自己的
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path=value["path"] #得到图片的存放路径
            item["url_path"]=image_file_path
        return item'''