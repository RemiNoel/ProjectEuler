# An irrational decimal fraction is created by concatenating the positive integers:
#
# 		0.123456789101112131415161718192021...
#					 ^
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d[n] represents the nth digit of the fractional part, find the value of the following expression.
#
# 		d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]
#

# The formula can be digitalized based on the infinite series : https://en.wikipedia.org/wiki/Champernowne_constant
# Takes too much time to compute large digits


'''
def champernowneFormula(n=1000001):
	num = 0
	t_term = 0
	for i in range(1, n):
		for k in range(10**(n-1), 10**n - 1):
			for t in range(1, n - 1):
				t_term += 10**(t - 1) * t
			num += k / 10**(n * (k - 10**(n-1) + 1) + 9 * t_term)
	return num
'''

def main():
    C = ''
    finalNumber = 1

    for i in range(400000):
        C += str(i)
        if len(C) > 1000000:
            break

    cList = list(C)

    for i in range(7):
        finalNumber *= (int(cList[10**i]))

    print(finalNumber)

if __name__ == '__main__':
    main()