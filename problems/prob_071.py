################################################################################
#                          Project Euler Problem 071                           #
#                     https://projecteuler.net/problem=071                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 13, 2020                                                  #
################################################################################

def prob_071(LIMIT=10**6):
    below = math.floor(Fraction(3,7) * LIMIT)
    return below-1 

prob_071()