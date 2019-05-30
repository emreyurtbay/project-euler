# Project Euler Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math 
import time

def is_prime(n):
	'''
	Function determines if a number is prime
	'''
	flag = True

	if n == 2:
		return True
	else:
		for i in xrange(2, n/2):
			if n%i == 0:
				flag = False
				break
		return flag


def SolveEuler3(n):
	'''
	Finds the largest prime factor of a number
	'''
	lst = []
	for low in xrange(2, int(math.sqrt(n))+1):
		if n % low == 0 and is_prime(low):
			lst.append(low)

			hi = n / low
			if is_prime(hi):
				lst.append(hi)

	return max(lst)


start = time.time()
answer =  SolveEuler3(600851475143)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (answer,elapsed)

### found 6857 in 0.118443012238 seconds.
