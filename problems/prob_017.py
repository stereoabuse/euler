################################################################################
#                          Project Euler Problem 017                           #
#                     https://projecteuler.net/problem=017                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_017():
    '''Returns number of letters if 1-1000 were written out...
    thank god for python libraries'''
    ans = 0
    for i in range(1, 1001):
        count = len(num2words(i).replace(' ','').replace('-',''))
        ans += count
    return ans 

prob_017()