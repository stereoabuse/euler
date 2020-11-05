################################################################################
#                          Project Euler Problem 102                           #
#                     https://projecteuler.net/problem=102                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_102():
    path = 'utility/euler_102_triangles.txt'
    total,px,py = 0,0,0
    for tri in open(path):
        (ax,ay,bx,by,cx,cy) = [int(point) for point in tri.split(",")]
        abc,pbc = abs((ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))/2),abs((px*(by-cy)+bx*(cy-py)+cx*(py-by))/2)
        apc,abp = abs((ax*(py-cy)+px*(cy-ay)+cx*(ay-py))/2),abs((ax*(by-py)+bx*(py-ay)+px*(ay-by))/2)
        if abc == pbc + apc + abp:
            total+=1
    return total

prob_102()