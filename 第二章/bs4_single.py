#@Time ： 2022/3/23/023 12:31
#@Author : xukang


from bs4 import BeautifulSoup
import requests
import csv

csvFile = open("synk2.csv", "r")
reader = csv.reader(csvFile)

# 建立空字典
result =[]
for item in reader:
    print('+'.join(item))
    result.append('+'.join(item))

for herf in result:
    url = f"https://security.snyk.io/{herf}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)

# 解析数据
# 1.把页面源代码交给bs4处理，生成bs对象
    page = BeautifulSoup(resp.text, "html.parser")

    score = page.find("div",attrs={"data-snyk-test":"severity widget score"}).get("data-snyk-test-score")
    print(herf+"--score--" + score)

# 严重评级
# <span class="vue--badge__text" data-v-0f55f474="">high</span>
    severity_class=page.find("span",attrs={"class":"vue--badge__text"}).text.strip()
    print("severity_class:"+severity_class)

# 发布日期
# <h4 data-snyk-test="formatted-date" class="vue--heading date" data-v-8dd2f746="" data-v-5d5a081c="">
#     Introduced: 11 Mar 2022
# #   </h4>
#     formatted_date = page.find("h4",attrs={"data-snyk-test":"formatted-date"}).text.strip()
#     print("formatted_date:"+formatted_date[12:])

# markdown-description
# # <div class="vue--markdown-to-html markdown-description" data-v-185c2450="" data-v-75cf0f30="" data-v-6b6ff1c7="">
# # <p>Upgrade <code>simple-git</code> to version 3.3.0 or higher.</p>
# # </div>
    markdown_description =page.find("div",attrs={"class":"vue--markdown-to-html markdown-description"}).text.strip()
    print("markdown_description:"+markdown_description)
