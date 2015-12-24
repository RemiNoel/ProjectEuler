# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def isDigitFactorial(testNum, factTable):
	sumOfFactDigit = 0
	tempNum = testNum

	# Get each digits of testNum and add its factorial values to sumOfFactDigit. 
	while tempNum > 0:
		temp = tempNum % 10
		tempNum = tempNum // 10
		sumOfFactDigit += factTable[temp]

	# Verify if it's a 'curious' number
	if sumOfFactDigit == testNum:
		return True
	return False


def main():
	sumNum = 0
	factTable = []

	# Calculate the factorial value of each digits
	for x in range(0, 10):
		factTable.append(factorial(x))

	# Max loop limit : largest number which the factorial sum of its digit are of the same length as the number itself
	# 9!*7 = 2540160 -> 7 digits
	# 9!*8 = 2903040 -> 7 digits 
	for i in range(3, 2540161):
		if isDigitFactorial(i, factTable):
			sumNum += i

	print(sumNum)

if __name__== '__main__':
	main()
