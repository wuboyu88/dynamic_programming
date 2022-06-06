# 返回是否
# word_bank中的每个元素可以用无限多次
# 解题的关键：每次只比较prefix！
# m = len(target)
# n = len(word_bank)

# 1.递归
# 时间复杂度O(n^m*m)
# 空间复杂度O(m*m)


def all_construct(target, word_bank):
    if target == '':
        return [[]]
    result = []
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            tmp = all_construct(target[len(ele):], word_bank)
            tmp = map(lambda e: e + [ele], tmp)
            result += tmp
    return result


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('eee', ['e', 'ee', 'eee']))
print(all_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 2.动态规划
# 时间复杂度O(n*m*m)
# 空间复杂度O(m*m)


def all_construct(target, word_bank, memorization=None):
    if memorization is None:
        memorization = {}
    if target in memorization:
        return memorization[target]
    if target == '':
        return [[]]
    result = []
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            tmp = all_construct(target[len(ele):], word_bank, memorization)
            tmp = map(lambda e: e + [ele], tmp)
            result += tmp
    memorization[target] = result
    return memorization[target]


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('eee', ['e', 'ee', 'eee']))
print(all_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 3.迭代法
# 时间复杂度O(n*m*m)
# 空间复杂度O(m)


def all_construct(target, word_bank):
    result = [[] for _ in range(len(target) + 1)]
    result[0] = [[]]
    for i in range(len(target) + 1):
        for ele in word_bank:
            if i + len(ele) <= len(target):
                if target[i:i + len(ele)] == ele:
                    # Map is faster than list comprehension here.
                    result[i + len(ele)] = list(map(lambda e: e + [ele], result[i]))

    return result[len(target)]


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('eee', ['e', 'ee', 'eee']))
print(all_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))
