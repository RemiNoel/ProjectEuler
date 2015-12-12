# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can 
# be written as the sum of two abundant numbers is 24. By mathematical analysis, 
# it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number 
# that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def isPerfectNum(testNum):
	perfectSum = 0
	highestDiv = testNum // 2
	for i in range(1, highestDiv + 1):
		if testNum % i == 0:
			perfectSum += i
	if perfectSum == testNum:
		return True
	return False

def isDeficientNum(testNum):
	deficientSum = 0
	highestDiv = testNum // 2
	for i in range(1, highestDiv + 1):
		if testNum % i == 0:
			deficientSum += i
	if deficientSum < testNum:
		return True
	return False

def isAbundantNum(testNum):
	abundantSum = 0
	highestDiv = testNum // 2
	for i in range(1, highestDiv + 1):
		if testNum % i == 0:
			abundantSum += i
	if abundantSum > testNum:
		return True
	return False


abundantNums = set()
SumOfAllPosInt = 0

#	According to Wolfram Mathworld’s discussion on Abundant Numbers, 
# 	Every number greater than 20161 can be expressed as a sum of two abundant numbers. ” 
#	So our upper bound is 20161 instead of 28123.

for i in range(1, 20162):
	if isAbundantNum(i):
		abundantNums.add(i)

	# Check in the abundantNum set if 'i - a' is in there (a is an adundantNum). 
	# If not, 'i' can't be written as the sum of two adundant numbers	
	if not any((i - j) in abundantNums for j in abundantNums):
		SumOfAllPosInt += i
print(SumOfAllPosInt)