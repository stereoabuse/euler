################################################################################
#                          Project Euler Problem 063                           #
#                     https://projecteuler.net/problem=063                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_063():
    n_list = []
    for n in range(1,900):
        for i in range(1,500):
            if len(str(i**n)) == n:
                n_list.append(i**n)
    return len(n_list)

prob_063()