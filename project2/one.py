import re

'''
    re.split()

    str.split() 

    字符串的split只支持单个分隔符的处理。。对于多个分割符的情况无法作出处理。。
    这个时候 正则所提供的强大之处就是可以任意分隔。。。做到随心所欲不逾矩
'''

line = 'asd,asd asdh;sja.kah dfha  jfu ala'

l_list = re.split(r'[,.\s;]\s*', line)
print(l_list)