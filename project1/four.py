import operator

'''
    operator itemgetter
    接受的参数是一个可作为查询的标记。。
    可以接受dict的key， list 的 index , or 任何可以正确被 __getitem__()读取的值
    同时也可以传递多个参数到 itemgetter(), 
    会返回一个包含所有元素在内的元祖。。。。
    
    itemgetter 与 lambda 用法类似。
    但效率确实 lambad 的2.5倍左右。。
    

'''

rows = [
    {'fname': 'Brian', 'lname': 'jone', 'uid': 12},
    {'fname': 'Briadn', 'lname': 'jonea', 'uid': 11},
    {'fname': 'Brihn', 'lname': 'joner', 'uid': 17},
    {'fname': 'Bripn', 'lname': 'joneq', 'uid': 155},
    {'fname': 'Bripn', 'lname': 'joneq', 'uid': 152},
]

import logging
import time

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s %(filename)s [%(lineno)d] %(threadName)s  %(message)s',
                           datefmt='[%Y-%m-%d %A %H:%M:%S]',)
logging.info(time.time())
rows_by_fname = sorted(rows, key=operator.itemgetter('uid'))
logging.error(rows_by_fname)
logging.info(time.time())
#0.0002352
logging.info(time.time())
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
logging.error(rows_by_fname)
logging.info(time.time())
#0.000093