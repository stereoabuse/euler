################################################################################
#                          Project Euler Problem 042                           #
#                     https://projecteuler.net/problem=042                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_042():
    from utility.euler_042_words import wordlist
    numlist = []
    for word in wordlist:
        wordnum = 0
        for character in word:
            wordnum += ord(character.lower())-96
        numlist.append(wordnum)
    tri_set = set()
    for i in range(1,sorted(numlist)[-1]):
        tri_set.add(1/2 * i * (i + 1))
    
    return len(coded)

prob_042()