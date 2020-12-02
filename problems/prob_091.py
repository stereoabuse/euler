#
# Project Euler Problem 91
#


def prob_091(LIMIT=50):
    right_tri = 0 
    for x1 in range(0, LIMIT + 1):
        for x2 in range(0, LIMIT + 1):
            for y1 in range(0, LIMIT + 1):
                for y2 in range(0, LIMIT + 1):
                    P = (x1, y1)
                    Q = (x2, y2)
                    if len(set([O,P,Q])) == 3:
                        OP = ((P[0] - O[0]) ** 2 + (P[1] - O[1]) ** 2)
                        PQ = ((Q[0] - P[0]) ** 2 + (Q[1] - P[1]) ** 2)
                        QO = ((O[0] - Q[0]) ** 2 + (O[1] - Q[1]) ** 2)
                        a, b, c = sorted([OP, PQ, QO])
                        if a  + b  == c :
                            right_tri += 1
    return right_tri // 2

prob_091()