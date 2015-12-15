# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Developed an answer based on this Wolfram page : http://mathworld.wolfram.com/DecimalExpansion.html

# We can find the length of a recuring cycle by solving this expression : 10^k == 1(mod n) -> 10^k % n == 1(We use d instead of n in this code) 
#																		  					where k is the length of the recurring cycle
def recurCycle(d):
	for length in range(1, d):
		if 10**length % d == 1:
			return length
	return 0

def main():
	tempRecurCycle = 0
	longestRecurCycle = 0
	largestrecurCycleDiv = 0
	d = 1

	while d < 1000:
		tempRecurCycle = recurCycle(d)
		if tempRecurCycle > longestRecurCycle:
			longestRecurCycle = tempRecurCycle
			largestrecurCycleDiv = d
		d+=1
	print(largestrecurCycleDiv)

if __name__ == '__main__':
	main()