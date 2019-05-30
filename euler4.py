# Project Euler Problem 4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def get_products(digits):
	'''
	Function produces a list of products of every number with every other number up to 10^digits
	'''
	lis = []

	for i in range(10**digits):
		for j in range(10**digits):
			lis.append(str(i*j))

	return lis

def isPalindrome(num):
	'''
	Recursive Function to determine whether or not a string is a palindrome
	'''
	# base case
	if len(num) == 1:
		return True
	elif len(num) == 2 or len(num) == 3:
		if num[0] == num[-1]:
			return True
		else:
			return False

	# recursive case - Palindromes are determined from the middle of the string working outwards
	else:
		if isPalindrome(num[1:-1]) and (num[0] == num[-1]):
			return True
		else:
			return False


def SolveEuler4(digits):
	'''
	Function finds the max palindromic number in a list of products
	'''
	prods = get_products(digits)
	palindromes = []
	for prod in prods:
		if isPalindrome(prod):
			palindromes.append(int(prod))

	palindromes.sort()
	return palindromes[-1]


start = time.time()
answer =  SolveEuler4(3)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (answer,elapsed)


### found 906609 in 1.93076896667 seconds.
