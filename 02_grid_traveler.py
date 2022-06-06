# 1.递归
# 时间复杂度O(2^(m+n))
# 空间复杂度O(m+m)


def grid_traveler(m, n):
    if m == 1:
        return 1
    if n == 1:
        return 1
    return grid_traveler(m, n - 1) + grid_traveler(m - 1, n)


print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(18, 18))


# 2.动态规划
# 时间复杂度O(m*n)
# 空间复杂度O(m+n)
# 关键：用一个字典来记住已经算过的值，输入是原来的输入和memoization，输出是memoization的value


def grid_traveler(m, n, memoization=None):
    if memoization is None:
        memoization = {}
    if (m, n) in memoization:
        return memoization[(m, n)]
    if m == 1:
        return 1
    if n == 1:
        return 1
    memoization[(m, n)] = grid_traveler(m, n - 1, memoization) + grid_traveler(m - 1, n, memoization)
    return memoization[(m, n)]


print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(18, 18))


# 3.迭代法
# 时间复杂度O(m*n)
# 空间复杂度O(m*n)


def grid_traveler(m, n):
    result = [[0 for _ in range(n)] for _ in range(m)]
    result[0] = [1 for _ in range(n)]
    for i in range(m):
        result[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i][j - 1] + result[i - 1][j]
    return result[m - 1][n - 1]


print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(18, 18))
