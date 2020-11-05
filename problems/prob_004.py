################################################################################
#                          Project Euler Problem 004                           #
#                     https://projecteuler.net/problem=004                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_004(digits=3):
    "Returns largest palindrome made from product of two 3-digit numbers"
    n = 10 ** digits
    biglist = []
    for i in range(n):
        for j in range(i,n):
            if str(i*j) == "".join(reversed(str(i*j))):
                biglist.append(i*j)
    return sorted(biglist)[-1]

prob_004()