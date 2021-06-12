################################################################################
#                          Project Euler Problem 060                           #
#                     https://projecteuler.net/problem=060                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     June 12, 2021                                                      #
################################################################################

def prob_60():


    big_prime_set = set(sieve(99999999))

    primes = euler_funcs.sieve(9999)
    possible = []
    second_round_possible = []
    third_round_possible = []
    fourth_round_possible = []
    sums = []


    for combo in combinations(primes, 2):
        if all(is_prime(concat(x,y)) for x,y in permutations(combo,2)):
            possible.append(list(combo))

    for prime in primes:
        for combo in possible:
            if all(concat(x,y) in big_prime_set for x,y in permutations(combo + [prime],2)):
                second_round_possible.append(combo + [prime])

    for prime in primes:
        for combo in second_round_possible:
            if all(concat(x,y) in big_prime_set for x,y in permutations(combo + [prime],2)):
                third_round_possible.append(combo + [prime]) 

    for index, prime in enumerate(primes):
        for combo in third_round_possible:
            if all(concat(x,y) in big_prime_set for x,y in permutations(combo + [prime],2)):
                fourth_round_possible.append(combo + [prime])

    for group in fourth_round_possible:
        sums.append(sum(group))

    return min(sums)

print(prob_60())