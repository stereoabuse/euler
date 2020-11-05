################################################################################
#                          Project Euler Problem 043                           #
#                     https://projecteuler.net/problem=043                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_043():
    pandigits = list(permutations('9876543210'))
    pandigitals, pandigstrings = [], []
    for row in pandigits:
        pandigitals.append(int(''.join(row)))
        pandigstrings.append(''.join(row))
    bigsum = 0
    for item in pandigstrings:
        if 0 == (int(item[1:4]) % 2) == (int(item[2:5]) % 3) == \
        (int(item[3:6]) % 5) == (int(item[4:7]) % 7) == (int(item[5:8]) % 11)\
        == (int(item[6:9]) % 13) == (int(item[7:10]) % 17):
            bigsum += int(item)

    return bigsum

prob_043()