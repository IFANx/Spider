#@Time ： 2021/8/2/002 17:10
#@Author : xukang

import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入需要翻译的英文单词")

data={
    "kw": s
}
#发送post请求
resp=requests.post(url,data=data)
print(resp.json())
resp.close()