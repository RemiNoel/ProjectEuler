# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isBinPalindrome(num):
	# Change num to binary then remove 0b from the start of the new binary num
	binStr = str(bin(num))[2:]
	return binStr == binStr[::-1]

def isDecPalindrome(num):
	strNum = str(num)
	return strNum == strNum[::-1]

def decPalindromeGen(start, end):
	for i in range(start, end):
		if isDecPalindrome(i):
			yield i

def main():
	sumPalindrome = 0

	# loop through base-10 palindrome to save resources
	for decPalindrome in decPalindromeGen(1, 1000000):
		if isBinPalindrome(decPalindrome):
			sumPalindrome += decPalindrome

	print(sumPalindrome)


if __name__ == '__main__':
	main()