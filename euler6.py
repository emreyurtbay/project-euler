"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""
import time

def sumOfSquares(num):
	"""
	Finds the sum of squares of the natural numbers up to the variable num
	"""
	mySum = 0

	rangeLimit = num + 1

	# Python starts at 0
	for i in range(rangeLimit):
		x = i**2
		mySum += x

	return mySum

def squareOfSum(num):
	"""
	Finds the square of the sum of the numbers up to the variable num
	"""

	mySum = 0

	rangeLimit = num + 1

	# python starts at 0
	for i in range(rangeLimit):
		mySum += i

	return mySum**2

def solve(num):
	return squareOfSum(num) - sumOfSquares(num) 


start = time.time()
answer =  solve(100)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (answer,elapsed)

# found 25164150 in 3.91006469727e-05 seconds.
