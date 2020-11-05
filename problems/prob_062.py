################################################################################
#                          Project Euler Problem 062                           #
#                     https://projecteuler.net/problem=062                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_062():
    d = {}
    for i in range(300, 10000):
        tripled = ''.join(sorted(str(i ** 3)))
        if not tripled in d:
            d[tripled] = []
            d[tripled].append(i)
        else:
            d[tripled].append(i)
    return sorted(d.items(), key=lambda x:len(x[1]), reverse=True)[0][1][0] ** 3

prob_062()