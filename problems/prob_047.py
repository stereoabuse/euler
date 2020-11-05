################################################################################
#                          Project Euler Problem 047                           #
#                     https://projecteuler.net/problem=047                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_047():
    primes = set(euler_funcs.seive(350))
    biglist = set()
    for i in primes:
        for j in primes:
            for k in primes:
                for m in primes:
                    biglist.add(i*j*k*m)
                    biglist.add(i*j*k*m*i)
                    biglist.add(i*j*k*m*j)
                    biglist.add(i*j*k*m*k)
                    biglist.add(i*j*k*m*m)
    biglist = sorted(list(biglist))

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    for i in range(1,million):
        alist = set(prime_factors(i))
        blist = set(prime_factors(i+1))
        clist = set(prime_factors(i+2))
        dlist = set(prime_factors(i+3))
        if len(alist) == len(blist) == len(clist) == len(dlist)== 4:
                    return i


prob_047()