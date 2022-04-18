# @Time ： 2022/3/21/021 19:09
# @Author : xukang


import requests
import re
import csv

for it in range(0, 1):
    url = "https://security.snyk.io/vuln/SNYK-JS-URLPARSE-2412697"
    # url = "https://security.snyk.io/vuln/npm?search=url-parse"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text

    # 解析数据
    # obi = re.compile(
    #              r'data-snyk-test-score="(?P<point>.*?)"', re.S)
    obi = re.compile(
        r'<span data-snyk-test="vulnpage subtitle".*?class="vue--anchor" data-v-ce2707d6 data-v-0b00ea10>(?P<package>.*?)<!---->.*?'
        r'<div data-snyk-test="severity widget score".*?score="(?P<score>.*?)" class="severity-widget.*?'
        r'<span data-snyk-test="cve".*?data-v-5c275348>(?P<cve>.*?)<!---->.*?'
        r'<span data-snyk-test="cwe".*?data-v-5c275348>(?P<cwe>.*?)<!---->.*?'
        r'<p>Upgrade <code>(?P<package2>.*?)</code>(?P<advice>.*?)</p>'
        , re.S)
    # 字符串匹配
    res = obi.finditer(page_content)
    f = open("data1.csv",mode="a+",encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in res:
        if i.group("cve"):
            print(i.group("cve"))
        else:
            print("meiyou")
        # print(i.group("year").strip())
        # 变成字典存储
        dic=i.groupdict()
        # dic['cve'] = dic['cve'].strip()
        # 将字典中的一行写入csv
        csvwriter.writerow(dic.values())
f.close()
print("结束")
