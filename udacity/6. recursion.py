"""
Use of recursion using fibonacci series
"""


def get_fib(position: int) -> int:
    if position < 0:
        return -1
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)


print(get_fib(9))
print(get_fib(11))
print(get_fib(0))