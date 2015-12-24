# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
# simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import gcd

# all solutions will have the form (10*nom + i)/(10*i + den) = nom/den, where i is the number we want to cancel

def main():
	# find denominator product of the special fractions
	denProduct = 1
	nomProduct = 1
	
	for i in range(1, 10):
		for den in range(1, i):
			for nom in range(1, den):
				if (nom * 10 + i) * den == nom * (i * 10 + den):
					denProduct *= den
					nomProduct *= nom

	# Now we must reduce the resulting fraction to the lowest common terms
	denProduct /= gcd(nomProduct, denProduct)

	print(denProduct)		

if __name__== '__main__':
	main()
