# -*- coding:utf-8 -*-
__author__='bobby'

from scrapy.cmdline import execute

import sys
import  os

#将系统当前目录设置为项目根目录
#os.path.abspath(__file__)为当前文件所在绝对路径
#os.path.dirname为文件所在目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])
#执行命令，相当于在控制台cmd输入改名了