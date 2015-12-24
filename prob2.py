"""
@author: Austin Shin
https://projecteuler.net/problem=2
Even Fibonacci numbers
"""

def even_fib(n):
    """
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8
    This is defined tail-recursively through the use of a helper function.
    >>> even_fib(10)
    10 # 2+8
    """
    lst = []
    def even_fib_helper(prev, curr, final):
        if final < n:
            if final % 2 == 0:
                lst.append(final)
            return even_fib_helper(curr, prev+curr, prev+curr)
        else:
            return sum(lst)
    return even_fib_helper(0, 1, 0)

print(even_fib(4000000))
