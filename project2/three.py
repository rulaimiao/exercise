'''
    字符串替换

    str.replace() 简单的已经足够使用了

    re.sub()    可以进行正则替换，和复杂得文本替换

    re.subn()   基本类似，返回值增加一个，返回替换得次数

'''

import re
from calendar import month_abbr, month_name
text = 'Today is 01/11/2018, miaorulai is born in 09/08/1995'

text1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text1)

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

text2 = re.sub(r'(\d+)/(\d+)/(\d+)',change_date, text)
print(text2)
import datetime

_months = [datetime.date(2001, i+1, 1).strftime for i in range(12)]
_months.insert(0, lambda x: "")
for i in _months:
    print(i('%b'))


text3, n = re.subn(r'(\d+)/(\d+)/(\d+)',change_date, text)
print(text3)
print(n)

