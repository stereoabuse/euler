################################################################################
#                          Project Euler Problem 014                           #
#                     https://projecteuler.net/problem=014                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_014(n=million):
    "Returns longest Collatz chain under n"
    collatzs =[]
    for i in range(1,n):
        sequence_num = i
        count = 0
        while sequence_num != 1:
            if sequence_num % 2 == 0:
                sequence_num = sequence_num / 2
            else:
                sequence_num = 3* sequence_num + 1
            count += 1
        collatzs.append(tuple((count,i)))
    return sorted(collatzs, reverse = True)[:1][0][1]

prob_014()