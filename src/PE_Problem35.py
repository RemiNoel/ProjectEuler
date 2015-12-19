# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from math import sqrt, ceil

# 	Sieve of Eratosthenes Algorithm
def getPrimesBelowN(n = 1000000):
	"""Get all primes below n with the sieve of Eratosthenes. 
	@return: a list 0..n with boolean values that indicate if 
			i in 0..n is a prime.
	"""
	primes = [True] * n
	primes[0] = False
	primes[1] = False
	primeList = []
	roundUp = lambda n, prime: int(ceil(float(n) / prime))
	for currentPrime in range(2, n):
		if not primes[currentPrime]:
			continue
		primeList.append(currentPrime)
		for multiplicant in range(2, roundUp(n, currentPrime)):
			primes[multiplicant * currentPrime] = False
	return primes

def rotateString(pos, str_num):
	strRotated = str_num[pos:len(str_num)] + str_num[0:pos]
	return strRotated

def isCircularPrime(testNum, primeTable):
	# Check if number is prime then rotate.
	# Then do it for the length of the number
	# Return True if all the rotated numbers are prime nums
	
	strNum = str(testNum)
	for i in range(0, len(strNum)):
		rotatedStrNum = rotateString(i, strNum)
		if not primeTable[int(rotatedStrNum)]:
			return False
	return True


def main():
	numCircularPrime = 2
	maxLoopLimit = 1000000

	# Pre-load the primes below maxLoopLimit
	primeTable = getPrimesBelowN(maxLoopLimit)

	for prime, isPrimeNum in enumerate(primeTable):
		if (not isPrimeNum) or ("2" in str(prime)) or ("4" in str(prime)) or ("6" in str(prime)) or ("8" in str(prime)) or ("0" in str(prime)) or ("5" in str(prime)):	
			continue
			
		if isCircularPrime(prime, primeTable):
			numCircularPrime += 1

	print(numCircularPrime)

if __name__== '__main__':
	main()
