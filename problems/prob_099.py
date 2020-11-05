################################################################################
#                          Project Euler Problem 099                           #
#                     https://projecteuler.net/problem=099                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_099():
    lines = [line.strip().split(',') for line in open('utility/base_exp.txt', 'r').readlines()]
    greatest = 0
    top = ''
    for line in lines:
        if int(line[1]) * log(int(line[0]))> greatest:
            greatest = int(line[1]) * log(int(line[0]))
            top = line
    return lines.index(top) + 1

prob_099()