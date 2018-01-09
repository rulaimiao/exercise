
''' 

    collections namedtuple

'''

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('rulaimiao@163.com', '2018-01-09')
print(type(sub))
print(sub.addr)
print(sub.joined)

class Example():
    def __init__(self, addr):
        self.addr = addr

example1 = Example('china')
example2 = Example('Canada')
print(example2.addr)

Stock = namedtuple('Stock',['name', 'age', 'date'])
c = Stock('miaoxin', 12, '08/12/2018')
c = c._replace(**{'name': 'miaorulai'})
print(c)