################################################################################
#                          Project Euler Problem 025                           #
#                     https://projecteuler.net/problem=025                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_025(n=1000):
    '''Return index of fib sequence with length of n'''
    i = 1
    while True:
        a = fib_cached(i)
        if len(str(a)) == 1000:
            return i + 1
        i += 1

prob_025()