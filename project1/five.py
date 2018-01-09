import operator
import itertools


'''
    函数groupby()通过扫描序列找出拥有相同的值的序列项，并将他们分组

    （ps: groupby 只检查连续的项）

    只是为了坐分组的话我们可以使用 defaultdict()

    第二种对内存的使用量会很大
'''

rows = [
    {'address': 'China', 'date': '01/09/2018'},
    {'address': 'Canada', 'date': '01/08/2018'},
    {'address': 'Japan', 'date': '01/07/2018'},
    {'address': 'Canada', 'date': '01/05/2018'},
    {'address': 'Japan', 'date': '01/02/2018'},
    {'address': 'Canada', 'date': '01/08/2018'},
    {'address': 'Japan', 'date': '01/07/2018'},
    {'address': 'Canada', 'date': '01/09/2018'},
    {'address': 'Japan', 'date': '01/04/2018'},
    {'address': 'Canada', 'date': '01/06/2018'},
]


rows.sort(key=operator.itemgetter('date'))
print(rows)

for date, items in itertools.groupby(rows, key=operator.itemgetter('date')):
    print(date)
    for item in items:
        print('    ',item)

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)