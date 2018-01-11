from fnmatch import fnmatch, fnmatchcase

'''
    fnmatch() 的匹配模式所采用的大小写区分规则和底层文件系统相同（根据操作系统的不同而有所不同）
                OS X 区分大小写
    fnmatchcase() 与fnmatch()的作用基本相同。。唯一不同的是它是完全按照我们的匹配规则来进行的匹配
    
    讲道理,个人感觉这个用处不是很大，除非是那种简单的应用场景，并且对性能还有要求（感觉这个东西对性能估计也没什么要求）
    就当个多余的知识点记录一下吧

'''

address = [
    '5412 N CLARK ST',
    '1060 E ADDISN ST',
    '1039 W GRANCILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

print([addr for addr in address if fnmatch(addr, '* ST')])

print([addr for addr in address if fnmatch(addr, '[1-2]*')])