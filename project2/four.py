'''
    不区分大小写的方式对文本做查找和替换
    re.I 不区分大小写
    re.D .匹配所有字符，包括换行符
    
'''
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
s = re.findall('python', text, flags=re.I)
print(s)

s1 = re.sub('python', 'snake', text, flags=re.I)
print(s1)
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

s2 = re.sub('python', matchcase('snake'), text, flags=re.I)
print(s2)

