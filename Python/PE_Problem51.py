'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:

            13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the
first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''

from math import sqrt


def isPrime(num):
    if type(num) == str:
        num = int(num)

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


# A prime number belongs to an eight prime family when the count of prime number generated from
# removing a digit to the base prime number is equal to 8
def eightPrimeFamily(primeNum, removeDigit):
    count = 0
    for digit in '0123456789':
        # Replaces all occurrences of old in string with new or at most max occurrences if max given.
        tempNum = int(str.replace(primeNum, removeDigit, digit))
        if tempNum > 100000 and isPrime(tempNum):
            count += 1
    return count == 8


def main():

    for i in getPrimes(100000, 1000000):
        tempStr = str(i)
        if tempStr.count('0') == 3 and eightPrimeFamily(tempStr, '0') or \
            tempStr.count('1') == 3 and eightPrimeFamily(tempStr, '1') or \
            tempStr.count('2') == 3 and eightPrimeFamily(tempStr, '2'):
            print(tempStr)

if __name__ == '__main__':
    main()
