################################################################################
#                          Project Euler Problem 052                           #
#                     https://projecteuler.net/problem=052                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_052(n=million):
    for i in range(1,n):
        if sorted(str(i)) == sorted(str(i*2))\
        and sorted(str(i*3)) == sorted(str(i*4))\
        and sorted(str(i*5)) == sorted(str(i*6))\
        and sorted(str(i)) == sorted(str(i*6)):
            return i

prob_052()