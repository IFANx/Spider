#@Time ： 2022/3/23/023 13:06
#@Author : xukang


from lxml import etree
import requests
from bs4 import BeautifulSoup

url = "https://security.snyk.io/vuln/SNYK-JS-CKEDITOR4-2430344"
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
resp = requests.get(url, headers=headers)
# print(resp.text)

# 解析数据

html = etree.HTML(resp.text)
print(html.xpath("/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div/h1/span/a/text()"))
