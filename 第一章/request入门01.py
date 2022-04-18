#@Time ： 2021/8/2/002 15:39
#@Author : xukang

# 安装requests
import requests

query=input("输入一个明星名")

url =f'https://www.sogou.com/web?query={query}'

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

resp=requests.get(url,headers=header) #添加请求头，反爬手段
print(resp.text) #获取页面源码
resp.close()