# @Time ： 2022/3/23/023 20:06
# @Author : xukang

import requests
import csv
from lxml import etree


# csv_file = 'synk2.csv'
def foo():
    with open('synk2.csv', 'r') as csvfile:
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


# 建立空字典
# result =[]
# for item in reader:
#     print('+'.join(item))
#     result.append('+'.join(item))


list = foo()
for herf in list:
    url = f"https://security.snyk.io/{herf}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)

    html = etree.HTML(resp.text)
    print(html.xpath("/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div/h1/span/a/text()"))

