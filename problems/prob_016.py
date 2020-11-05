################################################################################
#                          Project Euler Problem 016                           #
#                     https://projecteuler.net/problem=016                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_016():
    "Return sum of digits of 2 to the 1000"
    return sum(int(item) for item in [digit for digit in str(2**1000)])

prob_016()