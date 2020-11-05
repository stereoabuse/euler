################################################################################
#                          Project Euler Problem 036                           #
#                     https://projecteuler.net/problem=036                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_036(n=million):
    '''
    return sum of all numbers less than million that are 
    palidromic in base 10 and base 2
    '''
    pal_sum = [i for i in range(1,n) if str(i) == str(i)[::-1] \
               and bin(i)[2:] == bin(i)[:1:-1]]
    return sum(pal_sum)

prob_036()