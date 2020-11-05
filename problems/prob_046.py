################################################################################
#                          Project Euler Problem 046                           #
#                     https://projecteuler.net/problem=046                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_046(n=10000):
    primes = seive(n)
    odd_composite = []
    goldbach_nums = []
    for i in range(3,n,2):
        if i not in primes:
            odd_composite.append(i)
        for prime in primes:
            if prime < i:
                for square in range(1,int(sqrt(n))):
                    if i == prime + (2 *square**2) and i not in primes:
                        goldbach_nums.append(i)
    return [item for item in odd_composite if item not in goldbach_nums]

prob_046()