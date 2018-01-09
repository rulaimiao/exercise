import collections

'''
    找出序列中出现次数最多的元素

    collections Counter

    most_common

    update

    Counter 对于计数与表隔运算是一种非常棒的方式
'''

words = [1,2,3,4,5,2,1,23,4,1,23,1,2,34,2,5,1,4,5,6,1]

word_counts = collections.Counter(words)

print(word_counts.most_common(1))

print(word_counts[1])

morewords = [1,2,1,1,1]

word_counts.update(morewords)

print(word_counts[1])


words_two = [1,23,4,45,2,8,9,91,123,4,1,1]

word_counts_two = collections.Counter(words_two)

print(word_counts_two)

print(word_counts)

print(word_counts_two-word_counts)

print(word_counts_two + word_counts)

print(word_counts - word_counts_two)
