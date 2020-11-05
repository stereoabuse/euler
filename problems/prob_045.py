################################################################################
#                          Project Euler Problem 045                           #
#                     https://projecteuler.net/problem=045                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_045(n=million):
    tri_list, pent_list, hexag_list = [], [], []
    for i in range(1,n):
        tri_list.append(i*(i+1) / 2)
        pent_list.append(i*(3*i -1) / 2)
        hexag_list.append(i*(2*i -1))
    tri_pent = set(tri_list).intersection(pent_list)
    hex_pent_tri = set(tri_pent).intersection(hexag_list)
    return max(hex_pent_tri)

prob_045()