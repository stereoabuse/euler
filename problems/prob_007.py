################################################################################
#                          Project Euler Problem 007                           #
#                     https://projecteuler.net/problem=007                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 13, 2020                                                  #
################################################################################

def prob_007(LIMIT=10001):
    primes = 0
    n = 1
    while True:
        if is_prime(n):
            primes += 1
        if primes == LIMIT:
            return n
        n += 1

prob_007()