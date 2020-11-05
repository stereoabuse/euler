################################################################################
#                          Project Euler Problem 059                           #
#                     https://projecteuler.net/problem=059                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_059():
    
    words = [x.strip() for x in open('utility/59_frequency/words.txt').readlines()]
    cipher_url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
    cipher_text = [int(num) for num in requests.get(cipher_url).text.split(',')]
    letts = ascii_lowercase
    d = {}

    for l_0 in letts:
        for l_1 in letts:
            for l_2 in letts:
                s = ''
                count = 0
                for index, item in enumerate(cipher_text):
                    if index % 3 == 0:
                        s += chr(ord(l_0) ^ item)
                    if index % 3 == 1:
                        s += chr(ord(l_1) ^ item)
                    if index % 3 == 2:
                        s += chr(ord(l_2) ^ item)
                for word in words:
                    if word in s:
                        count += 1
                d[f'{l_0}{l_1}{l_2}'] = count
    best_fit = [k for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)][0]
    total = 0
    for index, item in enumerate(cipher_text):
        if index % 3 == 0:
            total += ord(best_fit[0]) ^ item
        if index % 3 == 1:
            total += ord(best_fit[1]) ^ item
        if index % 3 == 2:
            total += ord(best_fit[2]) ^ item
    return total

prob_059()