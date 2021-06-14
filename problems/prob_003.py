################################################################################
#                          Project Euler Problem 003                           #
#                     https://projecteuler.net/problem=003                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     June 14, 2021                                                      #
################################################################################

def prob_003(big_number=600851475143):
    "Returns largest prime factor of a big(ish) number"
    primes = sieve(int(big_number))
    for prime in primes[::-1]:
        if big_number % prime == 0:
            return prime
        
print(prob_003())
