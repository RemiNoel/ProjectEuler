# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
# simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import pdb


def main():
	# find denominator product of the special fractions
	denProduct = 1
	tempDigit = 0

	for num in range (10, 100):
		for den in range(num + 1, 100):
			if den % 10 != 0:
				listNum = [num // 10, num % 10]
				listDen = [den // 10, den % 10]
				
				# check in the list of num if one of the digits in listNum are the same and not both(all) the same
				# if True, remove it from the fraction. Then multiply the denominator(remaining digit in denList (pos 0)) to denProduct
				if any(i in listDen for i in listNum) and not all(i in listDen for i in listNum):
					if listNum[0] in listDen:
						tempDigit = listNum[0]
					else:
						tempDigit = listNum[1]
					listNum.remove(tempDigit)
					listDen.remove(tempDigit)

					if listNum[0] / listDen[0] == num/den:
						denProduct *= listDen[0]
	print(denProduct)		

if __name__== '__main__':
	main()
