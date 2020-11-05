################################################################################
#                          Project Euler Problem 002                           #
#                     https://projecteuler.net/problem=002                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_002(val=4*million):
    "Returns sum of even fibonacci's under val"
    a, b = 1, 2
    evenset = set()
    while b < val:
        if b % 2 == 0:
            evenset.add(b)
        a, b = b, a + b
    return sum(evenset)

prob_002()