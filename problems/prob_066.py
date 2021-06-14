################################################################################
#                          Project Euler Problem 066                           #
#                     https://projecteuler.net/problem=066                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     June 14, 2021                                                      #
################################################################################

from sympy.solvers.diophantine.diophantine import diop_bf_DN

def prob_066():
    
    biggest = (0,0,0)
    for D in range(1,1001):
        if diop_bf_DN(D,1)[0][0] > biggest[0]:
            biggest = (diop_bf_DN(D,1)[0][0], D, diop_bf_DN(D,1)[0][1])
    return biggest[1]

print(prob_066())