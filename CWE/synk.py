#@Time ： 2022/3/22/022 16:37
#@Author : xukang


#拿到页面源代码
# 通过re提取有效信息

import requests
import re
import csv

domainlist=[]
domain="https://security.snyk.io/"
for it in range(0,3):
    url = f"https://security.snyk.io/vuln/npm/?{it}"
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
    f = open("synk1.csv",mode="a+",encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in res:
        childdomain=domain+i.group("name")
        domainlist.append(childdomain)
        # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("rating").strip())
        dic=i.groupdict()
        # dic['name'] = dic['name'].strip()
        csvwriter.writerow(dic.values())
f.close()

for herf in domainlist:
    childpage=requests.get(herf,headers=headers)
    child_content = childpage.text
# 解析数据
    obi2 = re.compile(
        r'<span data-snyk-test="vulnpage subtitle".*?class="vue--anchor" data-v-ce2707d6 data-v-0b00ea10>(?P<package>.*?)<!---->.*?',re.S)

#字符串匹配
    reschild = obi2.finditer(child_content)
    f = open("child_P.csv",mode="a+",encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in reschild:
        dic = i.groupdict()
        csvwriter.writerow(dic.values())
f.close()
print("结束")
