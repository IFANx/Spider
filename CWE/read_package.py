#@Time ： 2022/3/25/025 16:54
#@Author : xukang
import os

import requests
import re

from bs4 import BeautifulSoup
from lxml import etree

def makedict():
    makedict = dict()
    with open('target_package_is-reachable_5ver','r') as f:
        for line in f.readlines():
            linecol = line.strip("\n")
            if not linecol.startswith('@'):
                list = linecol.split("@")
                # if not makedict.get(list1[0]):
                makedict[list[0]]=list[1]
                # else:
                #     makedict[list[0]].append(list1[1])
                for res in list:
                    print(res)
    return makedict

def gethtml():
    packagedict = makedict()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    for package in packagedict:
        domain = f"https://security.snyk.io/vuln/npm?search={package}"
        resp = requests.get(domain, headers=headers)
        page_content = resp.text
        savehtml(package,page_content)
        print("save:"+package)


def savehtml(file_name,file_content):
    path = "./html"
    f = open(file_name+".html", mode="a+", encoding="utf-8")
        # 写文件用bytes而不是str，所以要转码
    f.write(file_content)
    f.close()

def match():
    # xpath='//*[@id="sortable-table"]/tbody/tr/td[1]/a'
    path = "./html"
    files = os.listdir(path)
    s = []
    for file in files:
        f = open("./html/"+file, 'r',encoding="utf-8")
        pageinfo=f.read()
    # html = etree.HTML(pageinfo)
    # print(pageinfo)
        page = BeautifulSoup(pageinfo, "html.parser")
        # content = page.find("tbody", attrs={"class":"vue--table__tbody"}).get("a").get("herf")
        content = page.find("tbody", attrs={"class":"vue--table__tbody"})
        herf=[]
        package=[]
        if content:
            print(file+":"+content.text.strip())
            # herf=content.find("a", attrs={"class":"vue--anchor"}).get("herf")
            # package=content.find("a",attrs={"class":"vue--anchor"})
        else:
            print(file+":"+"NOTHING FOUND!!!")
        # if herf:
        #     print("herf:"+str(herf))
        # if package:
        #     # for res in package:
        #     print("package:"+str(package))
    # print(html.xpath(xpath))
    f.close()


if __name__ == "__main__":
    #1. 获取所有package包名
    # packagedict=makedict()

    # 2.获取对应的html页面信息
    # gethtml()
    # for package in packagedict:
        # print(packagedict[package]+package)
    # print(packagedict)

    #3.读取html文件
    match()







