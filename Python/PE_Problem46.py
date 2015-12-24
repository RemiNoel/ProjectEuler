'''
It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def main():
    notFound = True
    result = 0
    n = 5
    f = 1
    primeSet = set()

    while notFound:
        # Add to primeSet if n is a prime number
        if all(n % p for p in primeSet):
            primeSet.add(n)
        else:
            #Check that the composite numbers can't be written as the sum of a prime and twice a square
            if not any((n - 2*i**2) in primeSet for i in range(1, n)):
                notFound = False
                print(n)

        # This generates prime numbers on-the-go
        n += 3 - f
        f = -f


if __name__ == '__main__':
    main()
