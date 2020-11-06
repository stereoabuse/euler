################################################################################
#                          Project Euler Problem 023                           #
#                     https://projecteuler.net/problem=023                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_023(n = 28124):
    '''
    Return sum of all positive integers that can NOT
    be written as the sum of two abundant number
    https://en.wikipedia.org/wiki/Abundant_number
    '''
    abundant_list, non_sum = [], []
    int_list_sum = sum(range(1,n))

    double_abundants = set()
    for i in range(1,n):
        i_divisor_sum = sum(j for j in range(1, int(i/2) + 1) if i % j == 0)
        if i_divisor_sum > i:
            abundant_list.append(i)
    
    for x in abundant_list:
        for y in abundant_list:
            if y + x < n:
                double_abundants.add(x + y)
                
    return int_list_sum - sum(double_abundants)

prob_023()