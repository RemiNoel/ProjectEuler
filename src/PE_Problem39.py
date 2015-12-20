# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# 	there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

'''
we know : 	c^2 = a^2 + b^2
			perimeter = a + b + c

			therefore,
				c = perimeter - a - b

			Replacing in the first equation we get:
				(perimeter - a - b)^2 = a^2 + b^2
				perimeter^2 + a^2 + b^2 -2*perimeter*a - 2*perimeter*b + 2ab = a^2 + b^2

			thus,
				b = (perimeter^2 - 2*perimeter*a) / (2*perimeter*b - 2a)

Furthermore we know a < c and b < c and without loss of generality we can assume 
that a ≤ b (otherwise we could switch them) which gives us that a ≤ b < c.  
That implies a < p/3 and thus we don't need to check values higher than that.

We will verify every perimeter from 2 to 1000. Only even perimeter will be checked since
any combination of positive/negative a's and b' will result in a positive perimeter.

We can now use the equations above to find the values of a, b and c that respect a solution. 
If they all respect the solution, increment the perimeter value. 

If a new solution is found and the perimeter is higher then the last one: highestPer = per
Also, we need to store the index of highest set of {a,b,c}. 
So we will store in into the variable highestSetIndex.

We do not need to do anything with c because it is dependent of the variable a and b.
If we maximise a and b, c will also be maximised

'''

import math

def main():
	highestPer = 0
	highestNumSolutions = 0
	for per in range (2, 1001, 2):
		tempNumSolutions = 0
		for a in range(2, per // 3):
			# Check if 'b' is even. If so, c is also even thus perimeter. So it is a solution.
			b = per * (per - (2 * a)) % (2 * (per - a))
			if b == 0:
				tempNumSolutions += 1

		if tempNumSolutions > highestNumSolutions:
			highestNumSolutions = tempNumSolutions
			highestPer = per

	print(highestPer)	

if __name__ == '__main__':
	main()