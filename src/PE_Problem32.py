# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def isPandigital(num):
	str_num = str(num)
	return len(str_num) == 9 and not '1234567890'[:9].strip(num)

def main():
	pandList = set()

	for i in range(2, 60): # max range = 60 because it is the largest term when multiplied by 10000//i will give a 4-digit number
		if i < 10:
			start = 1234
		else:
			start = 123
		for j in range(start, 10000 // i):	# This will keep 5-digit products at bay. 
			if isPandigital(str(i) + str(j) + str(i*j)):
				pandList.add(i*j)

	print(sum(pandList))

if __name__ == '__main__':
	main()