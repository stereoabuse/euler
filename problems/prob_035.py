################################################################################
#                          Project Euler Problem 035                           #
#                     https://projecteuler.net/problem=035                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_035(n=million):
    '''
    A circular prime is a prime where each rotation of the 
    number is also a prime (197 -> 971 -> 719)
    
    Return number of circular primes below 1 million
    '''
    circs = set()
    primes = set(seive(n))
    for prime in primes:
        prime_str = str(prime)
        if all([int(prime_str[i:]+prime_str[:i]) in primes for i in range(len(prime_str))]):
                circs.add(prime)
    return len(circs)

prob_035()