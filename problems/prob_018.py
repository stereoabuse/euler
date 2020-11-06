################################################################################
#                          Project Euler Problem 018                           #
#                     https://projecteuler.net/problem=018                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_018():
    "Return max total top to bottom of triangle"
    nums = open('utility/euler_18_numbers.txt').readlines()
    tri = [[int(i) for i in r.split()] for r in nums][::-1]
    b = tri
    for i in range(len(tri[:-1])):
        n = [max(tri[i][m], tri[i][m+ 1]) for m, j in enumerate(tri[i][:-1])]
        b[i+1] = [sum(k) for k in zip(n, tri[i+1])]
    return max(b)[0]

prob_018()