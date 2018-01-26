'''
    处理unicode字符

    unicodedata.normalize()

    第一个参数是用来制定字符串的编码规范的
    NFC 代表使用全字符组成
    NFD 代表使用组合字符
    NFKC
    NFKD

    K 代表的是某种程度上相似的字符但是看起来不同的字符，会把他们同例化

    unicodedata.combining
'''
import unicodedata
import regex


s1 = 'Spicy Jalape\u00f1o'


s2 = 'Spicy Jalapen\u0303o'

print(s1,s2)

print(s1==s2)

t1 = unicodedata.normalize('NFD', s1)

t2 = unicodedata.normalize('NFC', s2)

t3 = unicodedata.normalize('NFD', s1)

t4 = unicodedata.normalize('NFD', s2)

print(t1, t2, t3, t4)

print(ascii(t1))
print(ascii(t2))
print(ascii(t3))
print(ascii(t4))
print(t1 == t2)
