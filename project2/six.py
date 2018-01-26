'''

'''

import sys
import unicodedata
import string

print(sys.maxunicode)

dightmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd' }
print(dightmap)


x = '\u0661'
print(x)
print(x.translate(dightmap))

s = '哈哈哈你'
print(s.translate(str.maketrans('哈你', '我爱', '你')))

print(s.translate(str.maketrans('哈你', '我爱')))