#@Time ： 2022/3/23/023 21:36
#@Author : xukang

import requests

# 112.6.117.178:8085
proxie = {
    "http" : "http://112.6.117.178:8085"
}
resp = requests.get("http://www.baidu.com", proxies=proxie)
# resp = requests.get("https://www.baidu.com")
resp.encoding ='utf-8'
print(resp.text)
