# 返回是否
# word_bank中的每个元素可以用无限多次
# 解题的关键：每次只比较prefix！
# m = len(target)
# n = len(word_bank)

# 1.递归
# 时间复杂度O(n^m*m)
# 空间复杂度O(m*m)


def count_construct(target, word_bank):
    if target == '':
        return 1
    result = 0
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            result += count_construct(target[len(ele):], word_bank)

    return result


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct('eee', ['e', 'ee', 'eee']))
print(count_construct('e' * 100, ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 2.动态规划
# 时间复杂度O(n*m*m)
# 空间复杂度O(m*m)


def count_construct(target, word_bank, memorization=None):
    if memorization is None:
        memorization = {}
    if target in memorization:
        return memorization[target]
    if target == '':
        return 1
    result = 0
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            result += count_construct(target[len(ele):], word_bank, memorization)
    memorization[target] = result
    return result


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct('eee', ['e', 'ee', 'eee']))
print(count_construct('e' * 100, ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 3.迭代法
# 时间复杂度O(n*m*m)
# 空间复杂度O(m)


def count_construct(target, word_bank):
    result = [0 for _ in range(len(target) + 1)]
    result[0] = 1
    for i in range(len(target) + 1):
        for ele in word_bank:
            if i + len(ele) <= len(target):
                if target[i:i + len(ele)] == ele:
                    result[i + len(ele)] += result[i]

    return result[len(target)]


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct('eee', ['e', 'ee', 'eee']))
print(count_construct('e' * 100, ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))
