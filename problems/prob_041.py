################################################################################
#                          Project Euler Problem 041                           #
#                     https://projecteuler.net/problem=041                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_041():
    nums = list(permutations('7654321'))
    oddnums = [int(''.join(i)) for i in nums if int(i[-1]) % 2 != 0]
    oddnums = sorted(oddnums, reverse=True)
    for i in oddnums:
        if is_prime(i):
            return i

prob_041()