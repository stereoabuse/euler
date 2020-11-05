################################################################################
#                          Project Euler Problem 038                           #
#                     https://projecteuler.net/problem=038                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_038():
    digits = [str(i) for i in range(1,10)]
    for i in range(10000,0,-1):
        number = str(i)+str(i*2)
        if len(number) == 9 and all(x in number for x in digits):
            return int(number)

prob_038()