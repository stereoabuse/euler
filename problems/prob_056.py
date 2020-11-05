################################################################################
#                          Project Euler Problem 056                           #
#                     https://projecteuler.net/problem=056                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_056(n=100):
    numbers, = [], []
    for a in range(1,n):
        for b in range(1,n):
            numbers.append(a**b)
    for number in numbers:
        digit_total = sum(int(digit) for digit in str(number))
        digitmaxes.append(digit_total)
    return sorted(digitmaxes, reverse=True)[0]

prob_056()