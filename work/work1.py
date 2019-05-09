#不添加close运行不会报错，是否有违反编译规则？
# try:
# 	f=open('text-file-process/log_files/201811113025.log',encoding='utf8')
# 	number_text=f.read()
# finally:
# 	if f:
# 		f.close()

import re

f=open('text-file-process/log_files/201811113025.log',encoding='utf8')
number_text=f.read()

f.close()

number = re.split(r'[\s,，：:]',number_text)

dic = {"201811113025":0}

for num in number:
    if num in dic:
        dic["201811113025"] += 1

print(dic["201811113025"])