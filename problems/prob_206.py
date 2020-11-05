################################################################################
#                          Project Euler Problem 206                           #
#                     https://projecteuler.net/problem=206                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_206():
    START = int(sqrt(1020304050607080900)) + 60
    STOP = int(sqrt(1929394959697989990))
    concealed = '1_2_3_4_5_6_7_8_9_0'
    concealed = [concealed[i] for i in range(0, len(concealed), 2)]

    for root in range(START, STOP, 100):
        square = str(root ** 2)
        square_part_list = [square[i] for i in range(0, len(square), 2)]
        if square_part_list == concealed:
            return root

prob_206()