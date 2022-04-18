#@Time ： 2022/3/21/021 18:32
#@Author : xukang

import re #正则表达式
import bs4 #网页解析
import urllib #
import xlwt #进行excel操作
def main():
#     1.爬取网页
#     2.解析数据
#     3.保存数据

    baseurl="https://movie.douban.com/top?250?start="
    datalist = getdata(baseurl)
    savepath=".\\douban.xls"
    saveData(savepath)
#爬取网页
def getdata(baseurl):
    datalist=[]
    return datalist

# 保存数据
def saveData(savepath):
    print("save....")

if __name__ =="__main__":
    main()
