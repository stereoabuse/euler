################################################################################
#                          Project Euler Problem 048                           #
#                     https://projecteuler.net/problem=048                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_048(n=1000):
    return int(str(sum(i**i for i in range(1, n+1)))[-10:])

prob_048()