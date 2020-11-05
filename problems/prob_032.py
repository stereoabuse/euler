################################################################################
#                          Project Euler Problem 032                           #
#                     https://projecteuler.net/problem=032                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_032():
    '''
    Return sum of produces whose mutiplicand,
    multiplier, produce identity can be written
    as a 1-9 pangidital
    '''
    digits = '123456789'
    products = set()
    for x in range(2000):
        for y in range(50):
            pdstring = str(x)+str(y)+str(x * y)
            if len(pdstring) == 9 and all(char in pdstring for char in digits):
                products.add(x*y)
    return sum(products)

prob_032()