################################################################################
#                          Project Euler Problem 719                           #
#                     https://projecteuler.net/problem=719                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     December 02, 2020                                                  #
################################################################################

def prob_719(N=10**12):
    
    def splitter(n):
        s = str(n)
        for i in range(1, len(s)):
            start = int(s[0:i])
            end = int(s[i:])
            yield (start, end)
            for split in splitter(end):
                result = [start]
                result.extend(split)
                yield result

    def is_S(n):
        'if the square root of the S number'
        for split in splitter(n**2):
            if sum(split) == n:
                return True
        return False     

    
    return sum(i**2 for i in range(1, int(sqrt(N) + 1)) if is_S(i))

prob_719()