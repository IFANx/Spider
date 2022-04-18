#@Time ： 2022/3/23/023 11:07
#@Author : xukang

import csv

# 读取csv至字典
csvFile = open("synk1.csv", "r")
reader = csv.reader(csvFile)

# 建立空字典
result =[]
for item in reader:
    result.append(item)
    print('+'.join(item))
print(result[0])

csvFile.close()

