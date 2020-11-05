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
    abundant_list, int_list, non_sum = [], [], []
    double_abundants = set()
    for i in range(1,n):
        i_divisor_sum = 0
        for j in range(1,int(i/2)+1):
            if i % j == 0:
                i_divisor_sum += j
        if i_divisor_sum > i:
            abundant_list.append(i)
    
    for value in abundant_list:
        for other_value in abundant_list:
            if other_value + value < n:
                double_abundants.add(value + other_value)
                
    for i in range(1, n):
        int_list.append(i)
    for i in int_list:
        if i not in double_abundants:
            non_sum.append(i)
    double_list = [i for i in double_abundants]

    return sum(int_list) - sum(double_list)

prob_023()