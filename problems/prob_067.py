################################################################################
#                          Project Euler Problem 067                           #
#                     https://projecteuler.net/problem=067                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_067():
    nums = open('utility/euler_67_numbers.txt').readlines()
    tri = [[int(i) for i in r.split()] for r in nums][::-1]
    b = tri
    for i in range(len(tri[:-1])):
        row = tri[i]
        n = [max(row[m], row[m+ 1]) for m, j in enumerate(row[:-1])]
        b[i+1] = [sum(k) for k in zip(n, tri[i+1])]
    return max(b)[0]

prob_067()