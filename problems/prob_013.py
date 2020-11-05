################################################################################
#                          Project Euler Problem 013                           #
#                     https://projecteuler.net/problem=013                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_013():
    "Returns the first ten digits of the sum of all the numbers in file"
    fh = open('utility/euler_13_numbers.txt')
    the_sum = 0
    for line in fh:
        the_sum += int(line)
        
    return int(str(the_sum)[0:10])

prob_013()