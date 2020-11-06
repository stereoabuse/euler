################################################################################
#                          Project Euler Problem 022                           #
#                     https://projecteuler.net/problem=022                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_022():
    '''return sum of ord(letter) * line number'''
    import utility.p022_names as namefile
    sorted_names = sorted(namefile.names)
    total, counter = 0, 1
    for name in sorted_names:
        name_value = sum((ord(letter) - 64) for letter in name)
        total += name_value * counter
        counter += 1
    return total

prob_022()