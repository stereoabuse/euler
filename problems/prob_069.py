################################################################################
#                          Project Euler Problem 069                           #
#                     https://projecteuler.net/problem=069                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_069(end=million):
    maximum = (0, 0)
    for n in range(1, end+1):
        if n / totient(n) > maximum[0]:
            maximum = (n / totient(n), n)

    return maximum

prob_069()