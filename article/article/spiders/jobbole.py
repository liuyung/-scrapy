# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import  Request
from urllib import parse
from article.items import jobboleaticleitem
#from article.utils.common import get_md5



class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/map/1.html']
    global j
    j=1
    def parse(self, response):
        #1.获取文章列表页中的文章URL并交给解析函数进行具体字段的解析
        #2.获取下一页的URL并交给scrapy进行下载，下载完成后交给parse
        post_urls=response.css("a[target='_blank']::attr(href)").extract()
        for  post_url in post_urls:
           #self.bookurl=parse.urljoin(response.url,post_url)
           yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail,)#parse可以自动拼接域名和网页地址
           #yield可以将url交给scrapy进行下载
        #提取下一页并交付给scrapy下载
        #next_url=response.css("")
        global j
        j=j+1
        if j<=9:
            next_url='http://www.quanshuwang.com/map/%s.html'%j
            print(next_url)
            if next_url:
                yield Request(url=next_url,callback=self.parse)



    def parse_detail(self,response):
        atticle_item=jobboleaticleitem()#实例化
        bookname=response.css("strong::text").extract()[0]
        bookauthor1=response.css("div.chapName span::text").extract()[0]
        bookauthor=bookauthor1.replace("作者：","")
        bookurl1=response.css("div.main-index a:nth-child(3)::attr(href)").extract()[0]
        bookurl=parse.urljoin(response.url,bookurl1)
        type=response.css("div.main-index a:nth-child(2)::text").extract()[0]
        atticle_item["bookname"]= bookname
        atticle_item["bookauthor"]= bookauthor
        atticle_item["type"]= type
        atticle_item["bookurl"]=bookurl
        #adasd["surl_fdf"]=get_md5(response)
        #atticle_item["url"]=response.url  #填充值    #图片地址的变量要转换成数组【】
        yield  atticle_item #下载后传递到pipelines.py里'''
        #提取文章的具体字段（回调函数）



