################################################################################
#                          Project Euler Problem 026                           #
#                     https://projecteuler.net/problem=026                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_026(d=1000):
    '''return value less than d for which 
        1/value contains the longest recurring
        cycle in its decimal fration part'''
    num = long = 1
    for number in range(3, d, 2):
        if number % 5 == 0:
            continue
        p = 1 
        while (10 ** p) % num != 1:
            p += 1
        if p > long:
            num, long = n, p
    return num

prob_026()