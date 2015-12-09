#	Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#	If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#	For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
#	The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#	Evaluate the sum of all the amicable numbers under 10000.

#	if d(a) == b and a != b and d(b) == a :
#		imcablepair++

from math import sqrt
import time
def d(n):
	sumOfdiv = 0
	for i in range(1,n):
		if(n % i == 0):
			sumOfdiv += i
	return sumOfdiv

start = time.time()
testNum = 10000
amicablePairSum = 0
tableOfPairs = []

_list = [d(i) for i in range(1, testNum + 1)]

for i in range(testNum):
	ind = _list[i]
	if i + 1 < ind and ind >= 1 and ind <= testNum and _list[ind - 1] == i + 1:
		tableOfPairs.append([i + 1, ind])

amicablePairSum = sum([sum(i) for i in tableOfPairs])
end = time.time()

print(amicablePairSum, end - start)
