################################################################################
#                          Project Euler Problem 030                           #
#                     https://projecteuler.net/problem=030                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_030(n=10*million):
    '''
    Return sum of all numbers that can be expresse
    as the sum of fifth powers of their digits
    '''
    dig_fith_list = []
    for i in range(2,n):
        digits_summed = 0
        for digit in map(int,str(i)):
            digits_summed += digit ** 5
        if digits_summed == i:
            dig_fith_list.append(i)
    return sum(dig_fith_list)

prob_030()