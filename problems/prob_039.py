################################################################################
#                          Project Euler Problem 039                           #
#                     https://projecteuler.net/problem=039                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_039(p=120):
    endlist = []
    for p in range(1001,100,-1):
        plist = []
        for a in range(500):
            for b in range(500):
                c = sqrt(a ** 2 + b **2)
                lengths = []
                if a + b + sqrt(a ** 2 + b ** 2) == p and (a**2 + b ** 2 == c ** 2):
                    lengths = sorted([a,b,c])
                    plist.append(len(lengths))
        endlist.append([p, len(plist)])
    return sorted(endlist, reverse=True, key=lambda x : x[1])[0][0]

prob_039()