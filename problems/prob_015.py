################################################################################
#                          Project Euler Problem 015                           #
#                     https://projecteuler.net/problem=015                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_015(n=20, m=20):
    "Returns number of routes through n by m grid"
    num = factorial(m+n)
    den = factorial(m) * factorial(n)
    return num // den

prob_015()