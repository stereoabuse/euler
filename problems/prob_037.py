################################################################################
#                          Project Euler Problem 037                           #
#                     https://projecteuler.net/problem=037                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_037(n=10*million):
    primes = set(seive(n))
    trunc = set()
    for prime in primes:
        ps = str(prime)
        if len(ps) > 1:
            if all([int(ps[i:]) in primes for i in range(len(ps))]) and all([int(ps[:len(ps)-i]) in primes for i in range(len(ps))]):
                trunc.add(prime)
    return sum(trunc)

prob_037()