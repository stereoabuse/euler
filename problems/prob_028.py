################################################################################
#                          Project Euler Problem 028                           #
#                     https://projecteuler.net/problem=028                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_028(SIDE=1001):
    '''Return sum of number on diagonal in SIDE x SIDE square'''
    mult, n, total = 0, 1, 1
    for _i in range(SIDE // 2):
        mult += 2
        for _j in range(4):
            n += mult
            total+= n
    return total

prob_028()