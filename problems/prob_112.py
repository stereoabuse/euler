################################################################################
#                          Project Euler Problem 112                           #
#                     https://projecteuler.net/problem=112                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_112():
    bounce_list = []
    i = 2
    while len(bounce_list)/(i-1) != .99:
        forward, reverse = [int(digit) for digit in str(i)], [int(digit) for digit in str(i)[::-1]]
        if not all(i <= j for i, j in zip(forward, forward[1:])) \
        and not all(i <= j for i, j in zip(reverse, reverse[1:])):
            bounce_list.append(i)
        i += 1
    return i-1

prob_112()