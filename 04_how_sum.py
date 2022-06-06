# 返回一个可能的数组
# numbers中的每个元素可以用无限多次
# numbers中的每个元素非负
# m = target_sum
# n = len(numbers)

# 1.递归
# 时间复杂度O(n^m*m)
# 空间复杂度O(m)


def how_sum(target_sum, numbers):
    if target_sum < 0:
        return None
    if target_sum == 0:
        return []
    for ele in numbers:
        tmp = how_sum(target_sum - ele, numbers)
        if tmp is not None:
            return [ele] + tmp
    return None


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [7, 14]))


# 2.动态规划
# 时间复杂度O(n*m*m)
# 空间复杂度O(m*m)


def how_sum(target_sum, numbers, memorization=None):
    if memorization is None:
        memorization = {}
    if target_sum in memorization:
        return memorization[target_sum]
    if target_sum < 0:
        return None
    if target_sum == 0:
        return []
    for ele in numbers:
        tmp = how_sum(target_sum - ele, numbers, memorization)
        if tmp is not None:
            memorization[target_sum] = [ele] + tmp
            return memorization[target_sum]
    memorization[target_sum] = None
    return memorization[target_sum]


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [20, 30]))


# 3.迭代法
# 时间复杂度O(n*m)
# 空间复杂度O(m)


def how_sum(target_sum, numbers):
    result = [None for _ in range(target_sum + 1)]
    result[0] = []
    for i in range(target_sum + 1):
        if result[i] is not None:
            for ele in numbers:
                if i + ele <= target_sum:
                    result[i + ele] = result[i] + [ele]
    return result[target_sum]


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [7, 14]))
