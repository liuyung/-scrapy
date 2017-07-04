# -scrapy
利用scrapy框架搭建简单爬虫
idea文件夹是使用pycharm建工程时自动生成的文件夹
article为scrapy项目所在文件夹，article/main.py是用来运行这个项目的文件，article/article文件夹下面是实现逻辑。
spiders文件夹下写爬虫具体实现的逻辑，接着我们主要编辑article/article文件夹下的items.py、pipelines.py、setting.py三个文件。
       
       本爬虫实现爬取全书网http://www.quanshuwang.com/网站的小说名，对应的作者，小说类型，及对应的小说网址，并将数据以异步的方式保存在Mysql数据库中。尚有很大的优化空间。
