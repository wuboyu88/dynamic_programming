# 1.递归
# 时间复杂度O(2^n)
# 空间复杂度O(n)


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))

# 2.动态规划
# 时间复杂度O(n)
# 空间复杂度O(n)
# 关键：用一个字典来记住已经算过的值，输入是原来的输入和memoization，输出是memoization的value


def fibonacci(n, memoization=None):
    if memoization is None:
        memoization = {}
    if n in memoization:
        return memoization[n]
    if n <= 2:
        return 1
    memoization[n] = fibonacci(n-1, memoization)+fibonacci(n-2, memoization)
    return memoization[n]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))

# 3.迭代法
# 时间复杂度O(n)
# 空间复杂度O(n)


def fibonacci(n):
    result = [0 for _ in range(n)]
    result[0] = 1
    result[1] = 1
    for i in range(0, n-2):
        result[i+2] = result[i] + result[i+1]

    return result[-1]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))
