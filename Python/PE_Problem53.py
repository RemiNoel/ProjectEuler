'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5[C]3 = 10.

In general,

n[C]r =	    n!      ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
         r!(n−r)!

It is not until n = 23, that a value exceeds one-million: 23[C]10 = 1144066.

How many, not necessarily distinct, values of  n[C]r, for 1 ≤ n ≤ 100, are greater than one-million?
'''


def binomial(n, k):
    """
    Calculate C(n,k), the number of ways can k be chosen from n. Example:

    binomial(30,12)
    86493225
    """
    ways = 1
    for t in range(min(k, n - k)):
        ways = ways * (n - t) // (t + 1)
    return ways


# The problem can be solve using Pascal's triangle
# Each row of this triangle is vertically symmetric, so C(n, r) = C(n, n-r) and any C(n, x) for x from r to (n-r)
# is greater than C(n, r).

# If C(n, r) > 10^6 then C(n, x) for x from r to (n-r) will also > 10^6, therefore, the number of C(n, r) > 10^6,
# is simply (n-r)-r+1 for that row n.

def main():
    count = 0
    maxN = 100

    for n in range(23, maxN + 1):
        for r in range(2, n // 2 + 1):
            if binomial(n, r) > 10**6:
                count += n - 2 * r + 1
                break
    print(count)

if __name__ == '__main__':
    main()
