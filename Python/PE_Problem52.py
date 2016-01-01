'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''


def main():
    # The idea here is to create a function that will sort the digits of a number.
    # If every multiplier have the same digits, we have found our answer.
    # If not, increment by 9 the number we test and repeat.
    # We increment by 9 because any number and its permutation differ by a multiple of 9
    # E.g. : (45121-11542)/9 = 3731

    func = lambda num:sorted(str(num))

    # If we look at the resulting digits of 1/7 we can see that the repeating digits are :
    #
    #           1/7 = 0.142857 142857 142857...
    #           2/7 = 0.285714 285714 285714...
    #           ect.
    #
    # Instead of working with fractions, we'll start at 99999
    num = 99999

    while not func(num*2) == func(num*3) == func(num*4) == func(num*5) == func(num*6):
        num += 9

    print(num)

if __name__ == '__main__':
    main()
