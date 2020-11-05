################################################################################
#                          Project Euler Problem 034                           #
#                     https://projecteuler.net/problem=034                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_034(n=100000):
    '''
    Return sum of numbers equal to factorial of digits'''
    sum_of_sums = 0
    i_list = []
    for i in range(3,n+1):
        fact_sum = 0
        i_str = str(i)
        for character in i_str:
            fact_sum += factorial(int(character))
        if fact_sum == i:
            sum_of_sums += i
            i_list.append(fact_sum)
    return sum_of_sums

prob_034()