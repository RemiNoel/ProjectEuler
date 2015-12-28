'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from math import sqrt
from itertools import combinations


def isPrime(num):
    if num % 2 == 0 and num > 2:
        return False

    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def getPrimes(start, end):
    """
    Get all primes between start and end.
    """
    # This list will contain every 4-digit prime numbers
    primes = []

    for i in range(start, end):
        if isPrime(i):
            primes.append(i)
    return primes


def getDigits(strNum):
    if type(strNum) == int:
        strNum = str(strNum)
    listOfDigits = [i for i in strNum]
    return listOfDigits


def main():
    # This list will contain every 4-digit prime numbers
    primeNumbers = []

    # This list will contain, for each prime numbers, a list of digits that will be sorted
    L = []

    # This list will contain digits that appear for at least 3 primes
    recurantDigitList = []

    # This list will contain a list of at least 3 primes with the same 4 digits (Permutable numbers)
    listOfListsOfPrimes = []

    primeNumbers = getPrimes(1000, 10000)

    L = [getDigits(p) for p in primeNumbers]
    for i in range(len(L)):
        L[i].sort()
    L.sort()

    for i in range(len(primeNumbers) - 3):
        if L[i] == L[i + 1] and L[i + 1] == L[i + 2] and L[i + 2] == L[i + 3]:
            if L[i] not in recurantDigitList:
                recurantDigitList.append(L[i])

    # Create the list of lists
    for j in recurantDigitList:
        listOfListsOfPrimes.append([])

    # Store the permutable prime numbers into the list of lists
    for prime in primeNumbers:
        tempStr = getDigits(prime)
        tempStr.sort()
        if tempStr in recurantDigitList:
            tempIndex = recurantDigitList.index(tempStr)
            listOfListsOfPrimes[tempIndex].append(prime)

    # Check the list of lists to see if :
    # (i) each of the three terms are prime, and,
    # (ii) each of the 4-digit numbers are permutations of one another.
    for i in listOfListsOfPrimes:
        tempArray = combinations(i, 3)
        for j in tempArray:
            if j[1] - j[0] == j[2] - j[1]:
                print(str(j[0]) + str(j[1]) + str(j[2]))


if __name__ == '__main__':
    main()
