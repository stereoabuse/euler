################################################################################
#                          Project Euler Problem 054                           #
#                     https://projecteuler.net/problem=054                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     May 18, 2020                                                       #
################################################################################

def prob_054():
    
    # Poker card utility information
    with open('utility/p054_poker.txt') as file:
        hands = file.read().splitlines()
    cards = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    straights = [sorted(cards[c:c+5]) for c in range(0, len(cards)-4)]

    def values(hand):  return [cards.index(h[0]) for h in hand]
    def rank(counter): return cards.index(counter.most_common()[0][0])

    # player hands
    p1 = [sorted(hand.split()[:5]) for hand in hands]
    p2 = [sorted(hand.split()[5:]) for hand in hands]


    # These functions return a list of [True if this hand exists, high card value if exists]
    def one_pair(hand):
        c = Counter([h[0] for h in hand])
        exists = c.most_common()[0][1] == 2
        return [exists, rank(c) if exists else -1]

    def two_pair(hand):
        c = Counter([h[0] for h in hand])
        exists = c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2
        return [exists, rank(c) if exists else -1]

    def three_of_a_kind(hand):
        c = Counter([h[0] for h in hand])
        exists = c.most_common()[0][1] == 3
        return [exists, rank(c) if exists else -1]

    def straight(hand):
        exists = sorted([card[0] for card in hand]) in straights
        return [exists, max(values(hand)) if exists else -1]

    def flush(hand):
        c = Counter([h[1] for h in hand])
        exists = c.most_common()[0][1] == 5
        return [exists, max(values(hand)) if exists else -1]

    def full_house(hand):
        c = Counter([h[0] for h in hand])
        exists = c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2
        return [exists, max(values(hand)) if exists else -1]

    def four_of_a_kind(hand):
        c = Counter([h[0] for h in hand])
        exists = c.most_common()[0][1] == 4
        return [exists, rank(c) if exists else -1]

    def straight_flush(hand):
        exists = flush(hand)[0] and straight(hand)[0]
        return [exists, max(values(hand)) if exists else -1]

    def royal_flush(hand):
        exists = flush(hand)[0] and straight(hand)[0] and \
                 ('A' and 'T') in [card[0] for card in hand]
        return [exists, max(values(hand)) if exists else -1]

    def high_card(hand):
        return max([cards.index(c[0]) for c in hand])


    def points(hand):
        if royal_flush(hand)[0]:       return [9, royal_flush(hand)[1]]
        elif straight_flush(hand)[0]:  return [8, straight_flush(hand)[1]]
        elif four_of_a_kind(hand)[0]:  return [7, four_of_a_kind(hand)[1]]
        elif full_house(hand)[0]:      return [6, full_house(hand)[1]]
        elif flush(hand)[0]:           return [5, flush(hand)[1]]
        elif straight(hand)[0]:        return [4, straight(hand)[1]]
        elif three_of_a_kind(hand)[0]: return [3, three_of_a_kind(hand)[1]]
        elif two_pair(hand)[0]:        return [2, two_pair(hand)[1]]
        elif one_pair(hand)[0]:        return [1, one_pair(hand)[1]]
        else:                          return [-1, high_card(hand)]


    def p1_wins(p1_hand, p2_hand):
        if points(p1_hand)[0] >  points(p2_hand)[0] or \
        (points(p1_hand)[0] ==  points(p2_hand)[0] and \
         points(p1_hand)[1] >  points(p2_hand)[1]):
            return 1
        return 0
    
    return sum((p1_wins(p1[i], p2[i]) for i in range(len(hands))))

print(prob_054())
