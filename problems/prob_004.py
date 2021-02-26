################################################################################
#                          Project Euler Problem 004                           #
#                     https://projecteuler.net/problem=004                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     February 26, 2020                                                  #
################################################################################

def prob_004(limit=1000):
    "Returns largest palindrome made from product of two 3-digit numbers"
    largest = 0
    for i in range(limit):
        for j in range(i, limit):
            if str(i * j) == str(i * j)[::-1] and i * j > largest:
                largest = i * j
    return largest

prob_004()

