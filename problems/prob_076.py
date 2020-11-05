################################################################################
#                          Project Euler Problem 076                           #
#                     https://projecteuler.net/problem=076                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_076(n=100):
    numbers = set(range(1,100))
    parts = [1] + [0] * n
    for c in numbers:
        for i, x in enumerate(range(c, n + 1)):
            parts[x] += parts[i]
    return parts[n]

prob_076()