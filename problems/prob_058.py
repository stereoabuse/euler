################################################################################
#                          Project Euler Problem 058                           #
#                     https://projecteuler.net/problem=058                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_058():
    diag = []
    SIDE, ratio = 1, 1
    while ratio > .1:
        SIDE += 2
        diag = [1]
        multiplier = 0
        n = 1
        for _i in range(SIDE // 2):
            multiplier += 2
            for _j in range(4):
                n += multiplier
                if is_prime(n):
                    diag.append(n)
        ratio = len(diag) / (SIDE // 2 * 4 + 1)
    return SIDE

prob_058()


