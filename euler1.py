# Project Euler Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

def SolveEuler1(max_num):
	'''
	Function finds the sum of all the multiples of 3 or 5 below 1000
	'''

	answer = 0

	for i in range(max_num):

		if (i % 3 == 0) and (i % 5 == 0):
			answer += i
		elif i % 3 == 0:
			answer += i
		elif i % 5 == 0:
			answer += i

	return answer


start = time.time()
summation =  SolveEuler1(1000)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (summation,elapsed)


# found 233168 in 0.000426054000854 seconds.
