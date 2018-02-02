'''
文本对齐


> 代表右对齐
< 代表左对齐
^ 代表居中对齐
'''

import sys


text = 'Hello World'

s = text.ljust(20,'^')

print(s)

s1 = format(text, '*^20')

print(s1)


a = 'Hello ' 'World'

print(a)

print(text, s, s1, a, sep=',')

print(dir())
print('-------')
print(vars())
print('---------')
print(locals())


def sample():
    global s 
    s = 1
    s = 2 
    ss = 3
    cs = 4
    miao = 5
    print(vars())
    print(dir())
    print(locals())
    print(globals())

sample()



class safesub(dict):
    def missing(self, key):
        return '{'+ key +'}'

def sub(text):
    print(safesub(sys._getframe(1).f_locals))
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Miao rulai'
age = '18'


sss = 'You are {age}'
print(sub(sss))


# print(dict(sys._getframe(1).f_locals))



09081204Miao