#@Time ： 2022/3/29/029 15:39
#@Author : xukang

# 匹配JavaScript包
import os

import requests
from bs4 import BeautifulSoup


def makedict():
    with open('target_package_is-reachable_5ver','r') as f:
        makedict1 = dict()
        for line in f.readlines():
            linecol = line.strip("\n")
            if not linecol.startswith('@'):
                list1 = linecol.split("@")
                key = list1[0]
                val = list1[1]
                if key not in makedict1:
                    makedict1.setdefault(key,[]).append(val)
                else:
                    makedict1.setdefault(key,[]).append(val)
                print(key+":"+val)
    return makedict1

# 匹配所有包
def makedict2():
    with open('target_package_is-reachable_5ver','r') as f:
        makedict1 = dict()
        for line in f.readlines():
            linecol = line.strip("@")
            linecol=linecol.strip("\n")
            list1 = linecol.split("@",)
            key = list1[0]
            val = list1[1]
            if key not in makedict1:
                makedict1.setdefault(key,[]).append(val)
            else:
                makedict1.setdefault(key,[]).append(val)
            print(key+":"+val)
    return makedict1

# 获取所有html页面结果
def gethtml():
    packagedict = makedict2()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    for package in packagedict:
        domain = f"https://security.snyk.io/vuln/npm?search={package}"
        resp = requests.get(domain, headers=headers)
        page_content = resp.text
        savehtml(package,page_content)
        print("save:"+package)

#     保存html页面
def savehtml(file_name,file_content):
    f = open("html/"+file_name+".html", mode="a+", encoding="utf-8")
        # 写文件用bytes而不是str，所以要转码
    f.write(file_content)
    f.close()

# 读取文件夹中所有html文件，判断是否有npm漏洞

def match():
    # xpath='//*[@id="sortable-table"]/tbody/tr/td[1]/a'
    path = "./cve"
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
    packagedict = makedict2()
    # for key in packagedict:
    #     print(key)

    print(packagedict)
    # gethtml()
    # match()
