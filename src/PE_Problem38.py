# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#		192 × 1 = 192
#		192 × 2 = 384
#		192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
#	giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
#	the concatenated product of an integer with (1,2, ... , n) where n > 1?

def isPandigital(num):
	return len(str(num)) == 9 and not '1234567890'[:9].strip(str(num))

def concatenate(num, doubleNum):
	return int(str(num) + str(doubleNum))

def main():
	largestPandNum = 0
	concatenatedProduct = 0

	# All fixed number must contain less than 5 digits because n > 1
	# If the fixed number is 2 digit, we won't be able to generate a 9 digit number since n = 3 yields 
	# an 8 digit number and n = 4 yields a 11 digit number. Same foes for 3 digit numbers where we end at 7
	# or 11 digits in the result. That leaves us with a four digit number starting with 9
	n = 2

	# If the second digit > 4, then we get a carry over which results in the multiplying by 2 part will yield
	# 19xxx instead of 18xxx and thus we have two 9's which are not possible solutions. Further more non of the
	# the digits can be 1 since we will end up with a solution candidate with two 1's in it.
	# So the solution can be limited between 9234 and 9487 which means we would need to check 253 solutions.
	for i in range(9387, 9234, -1):
		largestPandNum = concatenate(i, n*i)
		if isPandigital(largestPandNum):
			break
	print(largestPandNum)

if __name__ == '__main__':
	main()