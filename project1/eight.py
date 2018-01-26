'''
    collection ChainMap
'''

from collections import ChainMap

a = {'x':1, 'y':2}
b = {'y':3, 'z': 4}

c = ChainMap(a,b)
print(c)
print(c['x'])
print(c['z'])
print(c['y'])

c = c.new_child({'x': 7})
print(c)
print(c['x'])

c = ChainMap(a, b)
c['y'] = 4
print(a['y'])
print(c)