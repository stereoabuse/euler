################################################################################
#                          Project Euler Problem 020                           #
#                     https://projecteuler.net/problem=020                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_020(n=100):
    "Returns sum of digits in 100!""
    total_factorial, total_sum = 1, 0
    for i in range(1,n):
        total_factorial *= i
    for j in str(total_factorial):
        total_sum += int(j)
    return total_sum

prob_020()