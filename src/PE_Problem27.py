# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
#
# Et turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# however, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
#
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# 	n² + an + b, where |a| < 1000 and |b| < 1000
#
# 	where |n| is the modulus/absolute value of n
# 	e.g. |11| = 11 and |−4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression that 
# produces the maximum number of primes for consecutive values of n, starting with n = 0.

import math

def quadFormula(n, a , b):
	return n**2 + a * n + b

def isPrime(num):
	if num % 2 == 0 and num > 2:
		return False

	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
			return False
	return True;

def main():
	bestA, bestB, bestCount = 0, 0, 0
	for a in range(-1000, 1001):
		for b in range(2, 1001): 
			if isPrime(b): 
				n = 0
				while isPrime(abs(quadFormula(n, a, b))):
					n += 1	
				if n > bestCount:
					bestCount = n
					bestA = a
					bestB = b	

	product = bestA * bestB
	print(str(bestA) + " and " + str(bestB) +" produces the maximum number of primes which is : " + str(bestCount))
	print('the product is : %s' % product)			

if __name__ == '__main__':
	main()