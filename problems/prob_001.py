################################################################################
#                          Project Euler Problem 001                           #
#                     https://projecteuler.net/problem=001                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_001(n=1000):
    "Returns sum of all multiples of 3 and 5 below n"
    mult_sum = 0
    for i in range (3, n):
        if i % 3 == 0 or i % 5 ==0:
            mult_sum += i
    return mult_sum

prob_001()