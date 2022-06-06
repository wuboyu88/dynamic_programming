# 返回是否
# word_bank中的每个元素可以用无限多次
# 解题的关键：每次只比较prefix！
# m = len(target)
# n = len(word_bank)

# 1.递归
# 时间复杂度O(n^m*m)
# 空间复杂度O(m*m)


def can_construct(target, word_bank):
    if target == '':
        return True
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            if can_construct(target[len(ele):], word_bank):
                return True
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 2.动态规划
# 时间复杂度O(n*m*m)
# 空间复杂度O(m*m)


def can_construct(target, word_bank, memorization=None):
    if memorization is None:
        memorization = {}
    if target in memorization:
        return memorization[target]
    if target == '':
        return True
    for ele in word_bank:
        if target[0:len(ele)] == ele:
            if can_construct(target[len(ele):], word_bank, memorization):
                memorization[target] = True
                return memorization[target]
    memorization[target] = False
    return memorization[target]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))


# 3.迭代法
# 时间复杂度O(n*m*m)
# 空间复杂度O(m)


def can_construct(target, word_bank):
    result = [False for _ in range(len(target) + 1)]
    result[0] = True
    for i in range(len(target) + 1):
        if result[i]:
            for ele in word_bank:
                if i + len(ele) <= len(target) and target[i:i + len(ele)] == ele:
                    result[i + len(ele)] = True

    return result[len(target)]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('e' * 1000 + 'f', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))
