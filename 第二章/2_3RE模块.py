#@Time ： 2021/8/3/003 10:34
#@Author : xukang

import re

# #findall: 匹配字符串中所有的复合正则的内容
# # list = re.findall(r"\d+","中国移动：10086，中国电信10010")
# # print(list)
# #
# #
# # #finditer:匹配字符串中的符合正则的内容，返回迭代器
# # it=re.finditer(r"\d+","中国移动：10086，中国电信10010")
# # for i in it:
# #     print(i.group())

# #search返回的结果是match对象，找到一个结果就返回，数据需要.group()
# s = re.search(r"\d+","中国移动：10086，中国电信10010")
# print(s.group())
#
#
# #match从头开始匹配
# m = re.match(r"\d+","10086，中国电信10010")
# print(m)

# 预加载正则表达式
# obj = re.compile(r"\d+")
#
# ret = obj.finditer("中国移动：10086，中国电信10010")
# for i in ret:
#     print(i.group())

s = """
<div class='jay'><span id='1'>中国联通1</span></div>
<div class='jj'><span id='2'>中国联通2</span></div>
<div class='jf'><span id='3'>中国联通3</span></div>
<div class='jd'><span id='4'>中国联通4</span></div>
<div class='jdd'><span id='5'>中国联通5</span></div>
"""

#(?P<分组名字>正则 可以单独从正则中匹配到进一步提取内容
obj = re.compile(r"<div class='(?P<id>.*?)'><span id='(?P<num>.*?)'>(?P<name>.*?)</span></div>", re.S)  #re.S:让.能匹配换行符

ret = obj.finditer(s)

for i in ret:
    print(i.group("id"))
    print(i.group("num"))
    print(i.group("name"))

