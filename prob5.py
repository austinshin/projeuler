"""
@author: Austin Shin
Problem 5: 2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

"""
Solved by pure brute force...
Answer: 232792560
"""
i = 4180

def checkFactors(x):
    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    j = [i for i in lst if x % i == 0]
    return (sum(j) == 210)

def divisByAll20(x):
    while (x < 10000000000):
        if (checkFactors(x)):
            print("Answer is :" + x)
            return
        x = x + 38
        print(x)
divisByAll20(i)        
