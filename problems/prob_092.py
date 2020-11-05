################################################################################
#                          Project Euler Problem 092                           #
#                     https://projecteuler.net/problem=092                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_092(LIMIT=10*million):
    
    def digit_chain(n):
        square_digit = sum(int(i) ** 2 for i in str(n))
        return square_digit
    
    eight_nines = 0
    for i in range(1,LIMIT):
        while True:
            if digit_chain(i) == 89:
                eight_nines += 1
                break
            elif digit_chain(i) == 1:
                break
            else:
                i = digit_chain(i)
    return eight_nines

prob_092()