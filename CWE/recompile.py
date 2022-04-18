#@Time ： 2022/3/22/022 20:49
#@Author : xukang

import re
import requests
import csv

# obi = re.compile(
#     r'<span data-snyk-test="vulnpage subtitle".*?class="vue--anchor" data-v-ce2707d6 data-v-0b00ea10>(?P<package>.*?)<!---->.*?'
#     r'<div data-snyk-test="severity widget score".*?score="(?P<score>.*?)" class="severity-widget.*?'
#     r'<span data-snyk-test="cve".*?data-v-5c275348>(?P<cve>.*?)<!---->.*?'
#     r'<span data-snyk-test="cwe".*?data-v-5c275348>(?P<cwe>.*?)<!---->.*?'
#     r'<p>Upgrade <code>(?P<package2>.*?)</code>(?P<advice>.*?)</p>'
#     , re.S)

url = f"https://security.snyk.io/vuln/SNYK-JS-SIMPLEGIT-2421199"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
resp = requests.get(url,headers=headers)
page_content=resp.text

# 定义每一个需要查找的正则，规范命名
heading_title = re.compile(r'<h1 class="vue--heading title" data-v-8dd2f746="" data-v-0b00ea10="" data-v-43af9ae8="">(?P<heading_title>.*?)span data-snyk-test="vulnpage subtitle"',re.S)

#字符串匹配
res = heading_title.finditer(page_content)
# f = open("synk1.csv",mode="a+",encoding="utf-8")
# csvwriter = csv.writer(f)
for i in res:
    print(i.group("heading_title").strip())
    # print(i.group("year").strip())
    # print(i.group("rating").strip())
    # dic=i.groupdict()
        # dic['name'] = dic['name'].strip()
    # csvwriter.writerow(dic.values())
# f.close()
