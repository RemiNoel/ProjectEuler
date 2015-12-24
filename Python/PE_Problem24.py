# A permutation is an ordered arrangement of objects. 
# or example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools

counter = 0
_str = '0123456789'
permLexPos = 1000000

tempPerm = itertools.permutations(_str, 10)

for i in tempPerm:
	counter += 1
	if counter == permLexPos:
		print(i)