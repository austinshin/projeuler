"""
@author: Austin Shin
https://projecteuler.net/problem=3
Largest prime factor
"""

def primes_sieve(lim):
    not_prime = []
    for i in range(2, lim + 1):
        if i not in not_prime:
            print(i)
            for j in range(i * 1, lim + 1, i):
                not_prime.append(j)
print(primes_sieve(100))
