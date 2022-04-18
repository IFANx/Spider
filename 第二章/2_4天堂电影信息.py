#@Time ： 2021/8/3/003 16:37
#@Author : xukang

#1.定位到2021电影
#2.从2021电影中提取子页面链接地址
#3.请求子页面链接地址，拿到想要的下载地址打包

import re
import csv
import requests

domian = "https://www.dytt89.com/"
# resp = requests.get(domian,verify=False) #verify=false 去掉安全验证
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
resp = requests.get(domian, headers=headers,verify=False)
resp.encoding = 'gb2312'
page_content = resp.text
print(resp.text)

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"a href='(?P<href>.*?)'.*?《(?P<name>.*?)》.*?</li>",re.S)
obj3 = re.compile(r'<div class="title_all"><h1>(?P<movie>.*?).*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)</tr>',re.S)

res1 = obj1.finditer(resp.text)
child_href_list = []
for i in res1:
    print(i.group('ul'))
    ul=i.group('ul')

#提取子页面链接
res2 = obj2.finditer(ul)
for j in res2:
    #拼接子页面链接
    child_href = domian + j.group('href').strip("/")
    child_href_list.append(child_href)

#提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding='gb2312'
    print(child_resp.text)
    res3 = obj3.search(child_resp.text)
    print(res3.group('movie'))
    print(res3.group('download'))
    break #测试用
