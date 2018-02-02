'''
有趣的字符串拼接操作示例

'''

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)