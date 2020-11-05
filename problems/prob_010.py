################################################################################
#                          Project Euler Problem 010                           #
#                     https://projecteuler.net/problem=010                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_010(n=2*million):
    "Returns the sum of all primes beneath n"
    numbers = set(range(n,1,-1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2,n+1,p)))
    return sum(primes)

prob_010()