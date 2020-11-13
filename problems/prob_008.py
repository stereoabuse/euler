################################################################################
#                          Project Euler Problem 008                           #
#                     https://projecteuler.net/problem=008                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 13, 2020                                                  #
################################################################################

def prob_008():
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    num_string = []
    for digit in str(n):
        num_string.append(digit)

    string_product = []
    for i in range(len(num_string) - 13):
        add_this = int(num_string[i]) * int(num_string[i +1]) * int(num_string[i+2]) * int(num_string[i +3]) * int(num_string[i + 4]) * int(num_string[i + 5]) * int(num_string[i+6]) * int(num_string[i +7]) * int(num_string[i + 8]) * int(num_string[i +9]) * int(num_string[i+10]) * int(num_string[i +11]) * int(num_string[i + 12])
        string_product.append(add_this)

    return sorted(string_product, reverse = True)[0]

prob_008()