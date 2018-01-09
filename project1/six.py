
'''
列表推导式适合简单的，数量较少的规则过滤
生成器表达式适合简单的，但是量大的规则过滤
内置函数 filter 对内容进行规则过滤，符合True 不符合 False, filter 过滤只能用于过掉不需要的
itertools.compress() 会接收一个可迭代对象以及一个布尔选择器序列·，输出时，他会给出所有在布尔选择器中为True的值
适合用于把一个序列的筛选结果施加到另一个序列中做提取
'''

alist = [1, 4, -5, 10, -7, 2, 3, -1]

blist = [n if n > 0 else 0 for n in alist ]

biter = (n if n > 0 else 0 for n in alist )
print(blist)
print(biter)
for i in biter:
    print(i)

def is_int(val):
    try:
        if val > 0:
            return True
        else:
            return False
    except ValueError:
        return False

clist = list(filter(is_int, alist))

print(clist)



