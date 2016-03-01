"""
@author: Austin Shin
"""

#Using Gauss's equation n(n+1)/2

def gauss_sum(n):
	return (n * (n+1)) / 2

def sum_square_difference(n):
	lst = []
	for x in range(1, 101):
		lst.append(x)

	lst2 = [i*i for i in lst]
	eachsquared = sum(lst2)

	sumto100 = gauss_sum(n)
	sumto100squared = sumto100 * sumto100

	return sumto100squared - eachsquared
