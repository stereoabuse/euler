################################################################################
#                          Project Euler Problem 087                           #
#                     https://projecteuler.net/problem=087                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_087(top=50*million):
    prime_squares = [i**2 for i in seive(int(top**(1/2)))]
    prime_cubes = [i ** 3 for i in seive(int(top**(1/3)))]
    prime_quads = [i ** 4 for i in seive(int(top**(1/4)))]
    ppts_2 = []
    for square in prime_squares:
        for cube in prime_cubes:
            for quad in prime_quads:
                if square + cube + quad < top:
                    ppts_2.append(square + cube + quad)
    return len(set(ppts_2))

prob_087()