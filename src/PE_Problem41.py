# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

from math import sqrt

def isPandigital(testNum, numLen):
    return len(str(testNum)) == numLen and not '1234567890'[:numLen].strip(str(testNum))

def isPrime(testNum):
    if type(testNum) == str:
        testNum = int(testNum)

    if testNum < 2:
        return False
    if testNum == 2:
        return True
    # Other even numbers are not primes
    if not testNum & 1:
        return False

    for i in range(3, int(sqrt(testNum)) + 1, 2):
        if testNum % i == 0:
            return False
    return True

def main():
    # Starting pandigital number:
    # The number of digit has to be between 4 and 9. (The number has to be larger then 2143)
    # Let's eliminate so value of n by using the divisibility rule tha any integer is divisible by 3
    # whose sum of digits is divisible by 3; therefore composite and not prime.
    # 9+8+7+6+5+4+3+2+1 = 45 % 3 = 0
    # 8+7+6+5+4+3+2+1   = 36 % 3 = 0
    # 7+6+5+4+3+2+1     = 28 % 3 = 1 (not composite)
    # 6+5+4+3+2+1       = 21 % 3 = 0
    # The starting number will be a 7 digit one. Also it must be pandigital.
    startPandigitalNum = 7654321

    while not (isPrime(startPandigitalNum) and isPandigital(startPandigitalNum, 7)):
        startPandigitalNum -= 2

    print(startPandigitalNum)

if __name__ == '__main__':
    main()