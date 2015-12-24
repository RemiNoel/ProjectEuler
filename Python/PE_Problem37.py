# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from math import sqrt
import re

def isPrime(testNum):
	if type(testNum) == str:
		testNum = int(testNum)

	if testNum < 2:
		return False
	if testNum == 2:
		return True
	# Other even numbers are not primes
	if not testNum & 1:
		return False

	for i in range(3, int(sqrt(testNum)) + 1, 2):
		if testNum % i == 0:
			return False
	return True	

def isTruncatePrime(testNum):
	# Check if number is prime then truncate the first number 
	# Then do it for the length of the number
	# Return True if all the truncated numbers are prime nums
	
	for i in range(1, len(str(testNum))):
		if not isPrime(str(testNum)[i:]) or not isPrime(str(testNum)[:i]):
			return False
	return True

def main():
	sumTruncPrimes = 0
	count = 0
	num = 11
	f = 1

	while count < 11:
		# We do not know what is the 11th truncPrime so we must create our own prime numbers
		# Formula to find prime nums is taken from the Sieve of Eratosthenes
		# http://www.askamathematician.com/2014/05/q-is-there-a-formula-for-finding-primes-do-primes-follow-a-pattern/
		num += 3 - f 
		f = -f

		# We leave the numbers under 100 because they are only 2 digits
		if not (num > 100 and re.search('[245680]', str(num))):		
			if isPrime(num) and isTruncatePrime(num):
				sumTruncPrimes += num
				count += 1

	print(sumTruncPrimes)


if __name__ == '__main__':
	main()
