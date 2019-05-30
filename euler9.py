# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

import time
import math

def generateEulersFormula():
	"""
	generates pythagorean triples
	"""
	myTrips = []
	for m in range(1, 10):
		for n in range(1, 10):
			a = m**2 -n**2
			b = 2*m*n
			c = m**2 + n**2
			if a > 0:
				myTuple = (a,b,c)
				myTrips.append(myTuple)
				n += 1
				if n >= m:
					break
		m += 1

	return myTrips

def solve(desiredSum):
	'''
	solves problem
	'''
	for triple in generateEulersFormula():
		mySum = 0
		while mySum < desiredSum + 5:
			for i in range(500):
				y = tuple([z * i for z in triple])
				a, b, c = y
				mySum = a + b + c
				if mySum == desiredSum:
					return (a*b*c, (a, b, c), a+b+c)

start = time.time()
prod =  solve(1000)
elapsed = (time.time() - start)
print "found %s in %s seconds." % (prod,elapsed)

"""
found (31875000, (375, 200, 425), 1000) in 0.00151491165161 seconds.
"""