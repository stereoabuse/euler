################################################################################
#                          Project Euler Problem 074                           #
#                     https://projecteuler.net/problem=074                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     December 02, 2020                                                  #
################################################################################

def prob_074(m=million):
    
    def digit_factorial(n):
        df = sum(factorial(int(i)) for i in str(n))
        return df

    total = 0
    for n in range(1, m):
        num = n
        chain = set()
        while num not in chain:
            chain.add(num)
            num = digit_factorial(num)
        if len(chain) == 60:
            total += 1
    return total

prob_074()