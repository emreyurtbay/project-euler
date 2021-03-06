# Project Euler Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import time

def fib(n):
	'''
	Finds the nth Fibonacci Number
	Indexing starts at 1 (i.e, the first fibonacci number is 1)
	'''
	if n == 1:
		return 1
	if n == 2:
		return 2
	else:
		return fib(n-1) + fib(n-2)

def SolveEuler2(max_num):
	'''
	Function finds the sum of the even fibonacci numbers whose values do not exceed max_num 
	'''
	max_fib = 0
	n = 1
	fib_lst = []

	while max_fib <= max_num:
		max_fib = fib(n)
		if max_fib % 2 == 0:
			fib_lst.append(max_fib)
		n += 1

	return sum(fib_lst)

start = time.time()
summation =  SolveEuler2(4000000)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (summation,elapsed)


#found 4613732 in 5.02194499969 seconds.
