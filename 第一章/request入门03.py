#@Time ： 2021/8/2/002 17:20
#@Author : xukang

import  requests

url="https://movie.douban.com/tag/#/?"
url2="https://read.douban.com/"

#重新封装参数
param = {
    "sort":"U",
    "range":"0,10",
    "tags":"",
    "start":"0",
    "genres":"喜剧"
}
header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

resp=requests.get(url2,headers=header)
print(resp.request.headers)
print(resp.text)
# reqs=requests.get(url=url,params=param,headers=header)
# print(reqs.request.headers)
# print(reqs.text)
# reqs.close()
resp.close()