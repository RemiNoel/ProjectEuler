# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 	1634 = 1^4 + 6^4 + 3^4 + 4^4
# 	8208 = 8^4 + 2^4 + 0^4 + 8^4
# 	9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def isSumOfFifthPowDigits(testNum):
	digit_1, digit_2, digit_3, digit_4, digit_5, digit_6 = 0, 0, 0, 0, 0, 0

	digit_1 = testNum % 10
	digit_2 = ((testNum % 100) - digit_1) / 10
	digit_3 = ((testNum % 1000 - 10 * digit_2) - digit_1) / 100
	digit_4 = ((testNum % 10000 - 100 * digit_3) - (10 * digit_2) - digit_1) / 1000
	digit_5 = ((testNum % 100000 - digit_4 * 1000) - (100 * digit_3) - (10 * digit_2) - digit_1) / 10000
	digit_6 = ((testNum % 1000000 - digit_5 * 10000) - (1000 * digit_4) - (100 * digit_3) - (10 * digit_2) - digit_1) / 100000

	powSumTestNum = digit_1**5 + digit_2**5 + digit_3**5 + digit_4**5 + digit_5**5 + digit_6**5

	if testNum == powSumTestNum:
		return True
	return False

def main():
	sumOfFifthPow = 0

	# Max loop limit = 9^5 * 6. With 7 digits, (9^5 * 7 gives a 6 digit number so 
	# the max limit will be the max limit of 6 digits sum of fifth pow digit (354294))
	for i in range(2, 354294):
		if isSumOfFifthPowDigits(i):
			sumOfFifthPow += i

	print(sumOfFifthPow)

if __name__ == '__main__':
	main()
