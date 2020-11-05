################################################################################
#                          Project Euler Problem 031                           #
#                     https://projecteuler.net/problem=031                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_031(n=200):
    '''Return number of ways to make 2pounds from coins'''
    coins = {1, 2, 5, 10, 20, 50, 100, 200}
    parts = [1] + [0] * n
    for c in coins:
        for i, x in enumerate(range(c, n + 1)):
            parts[x] += parts[i]
    return parts[n]

prob_031()