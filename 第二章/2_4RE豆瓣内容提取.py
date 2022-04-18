#@Time ： 2021/8/3/003 15:28
#@Author : xukang

#拿到页面源代码
# 通过re提取有效信息

import requests
import re
import csv

for it in range(0,250,25):
    url = f"https://movie.douban.com/top250?start={it}&filter="
    headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
    resp = requests.get(url,headers=headers)
    page_content=resp.text

#解析数据
    obi = re.compile(r'<li>.*?<div class="item">.*? <span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span property="v:best" content="(?P<rating>.*?)".*?'
                 r'<span>(?P<num>.*?)人评价</span>' , re.S)

#字符串匹配
    res = obi.finditer(page_content)
    f = open("data1.csv",mode="a+",encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in res:
        # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("rating").strip())
        dic=i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
f.close()
print("结束")
