################################################################################
#                          Project Euler Problem 055                           #
#                     https://projecteuler.net/problem=055                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_055(n=10000):
    ly = n
    for num in range(1,n+1):
        counter = 0
        while counter < 50:
            if num + int(str(num)[::-1]) == int(str(num + int(str(num)[::-1]))[::-1]):
                ly -=1
                counter = 50
            else:
                num += int(str(num)[::-1])
                counter += 1
    return ly

prob_055()