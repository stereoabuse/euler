################################################################################
#                          Project Euler Problem 019                           #
#                     https://projecteuler.net/problem=019                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_019(first_yr=1901, last_yr=2000): 
    "Return how many Sundays are on the 1st of the month in the 20th century"
    setfirstweekday(6)
    total = 0
    for year in range(first_yr, last_yr + 1):
        total += sum(1 for month in range(1, 12 + 1) if monthcalendar(year, month)[0][0] == 1)
    return total

prob_019()