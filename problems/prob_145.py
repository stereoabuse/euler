################################################################################
#                          Project Euler Problem 145                           #
#                     https://projecteuler.net/problem=145                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     December 02, 2020                                                  #
################################################################################

def prob_145(billion=10**9):
    
    def rev(n):
        rev_n = int(str(n)[::-1])
        sum_ = n + rev_n
        if (n or rev_n) % 10 == 0:
            return False
        return all(int(i) % 2 != 0 for i in str(sum_))
    
    return sum(1 for i in range(billion) if rev(i))

prob_145()