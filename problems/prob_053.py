################################################################################
#                          Project Euler Problem 053                           #
#                     https://projecteuler.net/problem=053                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_053(n=100):
    counter = 0
    for n in range(1,n+1):
        for r in range(1,n):
            if factorial(n)//(factorial(r)*factorial(n-r)) > million:
                counter += 1
    return counter

prob_053()