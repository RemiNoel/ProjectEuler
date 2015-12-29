'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from math import sqrt


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


def main():
    largestSumOfPrimes = 0
    primeSum = [0]
    numberOfTerms = 1

    primeNumbers = getPrimes(3, 1000000)


    for p in primeNumbers:
        primeSum.append(primeSum[-1] + p)
        if primeSum[-1] >= 1000000:
            break
    sumLen = len(primeSum)

    for i in range(sumLen):
        for j in range(sumLen - 1, i + numberOfTerms, -1):
            tempNum = primeSum[j] - primeSum[i]
            if j - i > numberOfTerms and isPrime(tempNum):
                numberOfTerms = j - i
                largestSumOfPrimes = tempNum
                break
    print(largestSumOfPrimes)

if __name__ == '__main__':
    main()
