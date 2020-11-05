################################################################################
#                          Project Euler Problem 040                           #
#                     https://projecteuler.net/problem=040                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_040():
    champ = ''
    for i in range(1,200000):
        i = str(i)
        champ+= i
    ans = int(champ[0])*int(champ[9])*\
            int(champ[99])*int(champ[999])\
            *int(champ[9999])*int(champ[99999])\
            *int(champ[999999])
    return ans

prob_040()