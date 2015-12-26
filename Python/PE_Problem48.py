'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''


def main():
    lastTenDigits = 0
    tempSum = 0

    for b in range(1, 1001):
        tempSum += b**b

    tempSum = str(tempSum)
    lastTenDigits = tempSum[len(tempSum) - 10:]

    print(lastTenDigits)

if __name__ == '__main__':
    main()
