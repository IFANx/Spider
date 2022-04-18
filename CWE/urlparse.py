#@Time ： 2022/3/22/022 16:37
#@Author : xukang


#拿到页面源代码
# 通过re提取有效信息

import requests
import re
import csv
from lxml import etree

# 获取url-pasre链接
def search(package):
    url = f"https://security.snyk.io/vuln/npm?search={package}"
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    resp = requests.get(url,headers=headers)
    page_content=resp.text

    #解析数据
    obi = re.compile(r'<tr class="vue--table__row".*?</ul>.*? <a href="(?P<name>.*?)" data-snyk-test.*?'
                     ,re.S)


    #字符串匹配
    res = obi.finditer(page_content)
    f = open("urlparse.csv",mode="a+",encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in res:
        dic=i.groupdict()
        csvwriter.writerow(dic.values())
    f.close()

    print("search结束")




def foo():
    with open('urlparse.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            href = row
            if href != []:
                yield href[0]


'''
csvFile = open("synk2.csv", "r")
reader = csv.reader(csvFile)
print(reader)
'''
def getinfo():
    list = foo()
    for herf in list:
        url = f"https://security.snyk.io/{herf}"
        # url = f"https://security.snyk.io/vuln/SNYK-JS-NORMALIZEURL-1296539"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        resp = requests.get(url, headers=headers)
        page_content = resp.text

        # xpath
        html = etree.HTML(resp.text)
        # print(html.xpath("/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div/h1/span/a/text()"))

        # f = open("data1.csv", mode="a+", encoding="utf-8")
        package = html.xpath("//*[@id='__layout']/div/main/div/div[1]/div[1]/div[1]/nav/ol/li[3]/span/text()")
        fault = html.xpath("//*[@id='__layout']/div/main/div/div[1]/div[2]/div/div/h1/text()")
        version = html.xpath("//*[@id='__layout']/div/main/div/div[1]/div[2]/div/div/h1/span/strong/text()")
        cve= html.xpath("/html/body/div[1]/div/div/main/div/div[2]/div[3]/div[1]/div[1]/span[1]/span/a/text()")
        cwe = html.xpath("/html/body/div[1]/div/div/main/div/div[2]/div[3]/div[1]/div[1]/span[2]/span/a/text()")
        score = html.xpath("/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/div")
        level = html.xpath("//*[@id='__layout']/div/main/div/div[2]/div[1]/div/div/span/span/text()")
        # print(package[0].strip())
        # print(fault[0].strip())
        print(type(version))
        # print(cve)
        # print(cwe)
        # print(score[0].get("data-snyk-test-score"))
        # print(level[0].strip())
        # f = open("data1.csv", mode="a+", encoding="utf-8")
        # csvwriter = csv.writer(f)
        #
        # csvwriter.writerow([package[0].strip(), fault[0].strip(), version, cve, cwe, score[0].get("data-snyk-test-score"), level[0].strip()])
        # f.close()


        # obi = re.compile(
        #     r'<span data-snyk-test="vulnpage subtitle".*?class="vue--anchor" data-v-ce2707d6 data-v-0b00ea10>(?P<package>.*?)<!---->.*?'
        #     r'<div data-snyk-test="severity widget score".*?score="(?P<score>.*?)" class="severity-widget.*?'
        #     r'<span class="vue--badge__text" data-v-0f55f474="">"(?P<level>.*?)"</span>.*?'
        #     r'<span data-snyk-test="cve".*?data-v-5c275348>(?P<cve>.*?)<!---->.*?'
        #     r'<span data-snyk-test="cwe".*?data-v-5c275348>(?P<cwe>.*?)<!---->.*?'
        #     r'</code>(?P<advice>.*?)</p>'
        #     , re.S)
        #  字符串匹配
        # res = obi.finditer(page_content)
        # f = open("data1.csv", mode="a+", encoding="utf-8")
        # csvwriter = csv.writer(f)
        # for i in res:
        #     if i.group("cve"):
        #         print(i.group("cve"))
        #     else:
        #         print("meiyou")
        #     # print(i.group("year").strip())
        #     # 变成字典存储
        #     dic = i.groupdict()
        #     # dic['cve'] = dic['cve'].strip()
        #     # 将字典中的一行写入csv
        #     csvwriter.writerow(dic.values())

    print("getinfo结束")
    print("test")


if __name__ == "__main__":
    # search("got")
    getinfo()
