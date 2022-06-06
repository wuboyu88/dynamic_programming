# 返回是否
# numbers中的每个元素可以用无限多次
# numbers中的每个元素非负
# m = target_sum
# n = len(numbers)

# 1.递归
# 时间复杂度O(n^m)
# 空间复杂度O(m)


def can_sum(target_sum, numbers):
    if target_sum < 0:
        return False
    if target_sum == 0:
        return True
    for ele in numbers:
        if can_sum(target_sum - ele, numbers):
            return True
    return False


print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(300, [7, 14]))


# 2.动态规划
# 时间复杂度O(n*m)
# 空间复杂度O(m)


def can_sum(target_sum, numbers, memoization=None):
    if memoization is None:
        memoization = {}
    if target_sum in memoization:
        return memoization[target_sum]
    if target_sum < 0:
        return False
    if target_sum == 0:
        return True
    for ele in numbers:
        if can_sum(target_sum - ele, numbers, memoization):
            memoization[target_sum] = True
            return memoization[target_sum]
    memoization[target_sum] = False
    return memoization[target_sum]


print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(300, [7, 14]))


# 3.迭代法
# 时间复杂度O(n*m)
# 空间复杂度O(m)


def can_sum(target_sum, numbers):
    result = [False for _ in range(target_sum + 1)]
    result[0] = True
    for i in range(target_sum):
        if result[i]:
            for ele in numbers:
                if i + ele <= target_sum:
                    result[i + ele] = True
    return result[target_sum]


print(can_sum(7, [5, 3, 4]))
print(can_sum(7, [2, 4]))
print(can_sum(300, [7, 14]))
