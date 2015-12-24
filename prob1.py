"""
@author: Austin Shin
https://projecteuler.net/problem=1
"""

def multiples(n):
    """
    >>> multiples(10)
    23
    """
    count, lst = 1, []
    while count < n:
        if (count % 3) == 0 or (count % 5) == 0:
            lst.append(count)
        count += 1
    return sum(lst)

print(multiples(1000))
