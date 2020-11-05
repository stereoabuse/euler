################################################################################
#                          Project Euler Problem 044                           #
#                     https://projecteuler.net/problem=044                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_044():
    pent_list = []
    pent_d = []
    for i in range(1,2999):
        pent_list.append(i*(3*i-1)//2)
    pent_set = set(pent_list)
    for pent1 in pent_set:
        for pent2 in pent_set:
            if (pent1 + pent2) in pent_set and (pent1 - pent2) in pent_set:
                pent_d.append(tuple((pent1-pent2,pent1,pent2)))
    return sorted(pent_d, reverse=True)[:1][0][0]

prob_044()