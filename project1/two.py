
'''
 slice 
 用来创建一个切片对象。。。
 作用：
 对代码中进行字符串，列表等提取的内容进行切片索引进行命名
 便于后期维护
'''

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
one = slice(2,8, 2)

s = items[one]
print(s)
print(one.start)
print(one.stop)
print(one.step)

two = slice(0, 10, 2)
ss = 'nishibushiwozuishenaideren'
sss = two.indices(len(ss))
print(type(sss))
print(sss)
for i in range(*sss):
    print(ss[i])