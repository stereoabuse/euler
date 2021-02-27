################################################################################
#                          Project Euler Problem 005                           #
#                     https://projecteuler.net/problem=005                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     February 26, 2020                                                  #
################################################################################

def prob_005(n=20):
    "Returns smallest number that is evenly divisible by all the numbers from 1 to n"
    ans = 1
    for i in range(1, n + 1):
        ans *= floor(i / gcd(i, ans))
    return ans

prob_005()