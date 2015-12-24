# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def main():
	countWays = 0
	twoPound = 200

	for i in range (twoPound, -1, -200):
		for j in range (i, -1, -100):
			for k in range (j, -1, -50):
				for m in range (k, -1, -20):
					for n in range (m, -1, -10):
						for q in range (n, -1, -5):
							for r in range (q, -1, -2):
								countWays += 1
	print(countWays)

if __name__ == '__main__':
	main()