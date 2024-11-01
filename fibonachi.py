# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fib(n-1)+fib(n-2)
#
# n = int(input('Enter: '))
# fib = fib(n)
# print(fib)
def fibonacci(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


#
n = int(input(""))
print(fibonacci(n))