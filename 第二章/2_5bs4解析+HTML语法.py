#@Time ： 2021/8/4/004 11:15
#@Author : xukang

import requests
from bs4 import BeautifulSoup

url = "https://book.douban.com/"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
resp = requests.get(url,headers=headers)
# print(resp.text)

#解析数据
#把页面源代码交给beautifulsoup处理，生成bs对象
page = BeautifulSoup(resp.text,"html.parser")
#2.从bs对象中查找数据
#find(标签，属性值)
table = page.find("div",attrs={"class":"title"}) #class是python关键字
print(table)


