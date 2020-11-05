################################################################################
#                          Project Euler Problem 021                           #
#                     https://projecteuler.net/problem=021                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_021(low=200,high=10000):
    '''
    Return sum of amicable numbers under 1000.
    https://en.wikipedia.org/wiki/Amicable_numbers
    '''
    newlist = []
    for i in range(low,high):
        i_list = []
        for j in range(1,int(i/2)+1):
            if i % j == 0:
                i_list.append(j)
        i_sum = sum(i_list)
        k_list = []
        for k in range(1,int(i_sum/2)+1):
            if i_sum % k == 0:
                k_list.append(k)
        k_sum = sum(k_list)
        if k_sum == i and i_sum!= k_sum:
            newlist.append(i)
    return sum(newlist)

prob_021()