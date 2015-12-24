'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''


# Factor a number into primes and frequency
def factor(testNum):
    """
    find the prime factors of n along with their frequencies. Example:
    factor(786456)
    [(2,3), (3,3), (11,1), (331,1)]
    """
    if testNum in [-1, 0, 1]:
        return []

    if testNum < 0:
        testNum = -testNum

    factorList = []
    while testNum != 1:
        p = trialDivision(testNum)
        e = 1
        testNum /= p
        while testNum % p == 0:
            e += 1
            testNum /= p
        factorList.append((p, e))
    factorList.sort()
    return factorList

# find the largest divisor of TestNum
def trialDivision(testNum, bound=None):
    if testNum == 1:
        return 1
    for p in [2, 3, 5]:
        if testNum % p == 0:
            return p
    if bound is None:
        bound = testNum

    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7
    i = 1

    while m <= bound and m * m <= testNum:
        if testNum % m == 0:
            return m
        m += dif[i % 8]
        i += 1
    return testNum


def main():
    notFound = True
    count = 0

    # First number that has four distinct prime factors
    n = 2 * 3 * 5 * 7

    while count != 4:
        n += 1

        if len(factor(n)) == 4:
            count += 1
        else:
            count = 0
    print(n - count + 1)


if __name__ == '__main__':
    main()
