def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

for i in dedupe([1,2,3,1,2,1,3,45,6,61,23,2,5,]):
    print(i)



# key 可以威一个方法，可以制定前面items中的重复策略，
# 当item为一个对象，或者一个字典的时候，
# 可以指定一个lamda来操作去重策略，并保持去重后数据的排序的稳定
def dedupe(items, key=None):
    seen = set()

    for item in items:
        if key:
            val = key(item)
        if val not in seen:
            yield item
            seen.add(item)   
