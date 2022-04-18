#@Time ： 2022/3/22/022 21:06
#@Author : xukang

from bs4 import BeautifulSoup
import requests
import csv


url = "https://security.snyk.io/vuln/SNYK-JS-SAILS-2428337"
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
resp = requests.get(url, headers=headers)

# 解析数据
# 1.把页面源代码交给bs4处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")

# 2.从bs4对象中寻找数据
# find & find_all
# cvef = page.find("span",attrs={"data-snyk-test":"cve"})
# cvef1=""
# if not cvef:
#     print("cvef is none")
# else:
#     cvef1 = cvef.find_all("a")
# cwef = page.find("span",attrs={"data-snyk-test":"cwe"}).find_all("a")
# main_title = title.find("span",attrs={"data-snyk-test":"vulnpage subtitle","class":"subheading"})
# sub_title = title.findall("a",attrs={"aria-describedby":"describedBy66AiOJVbKt"})
# if cvef1:
#     for cve in cvef1:
#         print(cve.get('id'))
# else:
#     print("cvef1 is none")

# for cwe in cwef:
#     print(cwe.get('id'))


# print(title)


# 错误类型
# <h1 class="vue--heading title" data-v-8dd2f746="" data-v-0b00ea10="" data-v-43af9ae8="">
#             Command Injection
#             <span data-snyk-test="vulnpage subtitle" class="subheading" data-v-8dd2f746="" data-v-0b00ea10="">
#               Affecting
#               <a aria-describedby="describedByySnHyE5udG" rel="noopener noreferrer" href="https://snyk.io/vuln/npm%3Asimple-git" target="_blank" class="vue--anchor" data-v-ce2707d6=""
#               data-v-0b00ea10="" data-v-8dd2f746="">simple-git<!---->
#               <span id="describedByrEQywyc5hz" data-snyk-test="BaseAnchor screen reader description" class="vue--anchor__offscreen" data-v-ce2707d6="">
#     Open this link in a new tab
#   </span></a>
#               package, versions
#               <strong data-snyk-test="vuln versions" data-v-8dd2f746="" data-v-0b00ea10="">
#                 &lt;3.3.0
#               </strong></span></h1>
# vue_heading_title = page.find("h1")
# package = vue_heading_title.find("a").text.strip()
# print(package)



# 评分
score = page.find("div",attrs={"data-snyk-test":"severity widget score"}).get("data-snyk-test-score")
print("score:" + score)

    # score=''
    # if scores:
    #     score = scores.get("data-snyk-test-score")

# 严重评级
# <span class="vue--badge__text" data-v-0f55f474="">high</span>
# severity_class=page.find("span",attrs={"class":"vue--badge__text"}).text.strip()
# print("severity_class:"+severity_class)
#

# 发布日期
# <h4 data-snyk-test="formatted-date" class="vue--heading date" data-v-8dd2f746="" data-v-5d5a081c="">
#     Introduced: 11 Mar 2022
# #   </h4>
formatted_date = page.find("h4",attrs={"data-snyk-test":"formatted-date"}).text.strip()
print("formatted_date:"+formatted_date[12:])


# markdown-description
# # <div class="vue--markdown-to-html markdown-description" data-v-185c2450="" data-v-75cf0f30="" data-v-6b6ff1c7="">
# # <p>Upgrade <code>simple-git</code> to version 3.3.0 or higher.</p>
# # </div>
# markdown_description =page.find("div",attrs={"class":"vue--markdown-to-html markdown-description"}).text.strip()
# print("markdown_description:"+markdown_description)


# overview
# <div class="vue--markdown-to-html markdown-description" data-v-185c2450="" data-v-75cf0f30="" data-v-6b6ff1c7=""><p><a href="https://www.npmjs.com/package/simple-git">simple-git</a> is a light weight interface for running git commands in any node.js application.</p>
# <p>Affected versions of this package are vulnerable to Command Injection via argument injection. When calling the <code>.fetch(remote, branch, handlerFn)</code> function, both the <code>remote</code> and <code>branch</code> parameters are passed to the <code>git fetch</code> subcommand. By injecting some git options it was possible to get arbitrary command execution.</p>
# </div>
# overviews = page.find("div",attrs={"class":"vue--markdown-to-html markdown-description"})
# print("overview:"+overviews.text)
#     f = open("bs4.csv", mode="a+", encoding="utf-8")
#     csvwriter = csv.writer(f)
#     if score:
#         print("score:" + score)
# csvwriter.writerow([score, severity_class, formatted_date, markdown_description])
#         csvwriter.writerow([score])
#     f.close()
print("over")
