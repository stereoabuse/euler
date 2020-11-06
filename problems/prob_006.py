################################################################################
#                          Project Euler Problem 006                           #
#                     https://projecteuler.net/problem=006                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_006(n=100):
    "Returns the difference between first one hundred natural numbers and the square of that sum"
    sum_of_squares = 0
    sums = 0
    for i in range(n+1):
        sum_of_squares += i**2
        sums += i
    square_of_sums = sums ** 2
    return abs(sum_of_squares- square_of_sums)

prob_006()