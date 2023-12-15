import time
import math

# 1 High Card: Highest value card.
# 8 One Pair: Two cards of the same value.
# 57 Two Pairs: Two different pairs.
# 400 Three of a Kind: Three cards of the same value.
# 2794 Straight: All cards are consecutive values.
# 19552 Flush: All cards of the same suit.
# 136858 Full House: Three of a kind and a pair.
# 958000 Four of a Kind: Four cards of the same value.
# 6705994 Straight Flush: All cards are consecutive values of same suit.
#  100 000 000 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

234624
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# T 10
# J 11
# Q 12
# K 13
# A 14
cards = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
    }

def PokerHand():
    result = 0

    hands = [[card for card in line.replace("\n","").split(" ")] for line in open("file/054_poker.txt")]

    for i in range(len(hands)):
        for j in range(len(hands[i])):
            hands[i][j] = [hands[i][j][1:], cards[hands[i][j][0]]]

    print(hands)
    
    for i in range(len(hands)):
        if playerOneWins(hands[i][:5], hands[i][5:]):
            result += 1

    return result

def playerOneWins(hand1, hand2):
    if handValue(hand1) > handValue(hand2):
        return True



def handValue(hand):
    point = 0
    card = 0

    while True:
        equalCards(hand)
        # if len(hand) == 5:
        #     hand, lp = RoyalFlush(hand)
        #     point+= lp
        
        # if len(hand) == 5:
        #     print()


def RoyalFlush(hand):
    suit = hand[0][0]
    for i in range(1,len(hand)):
        if hand[i][0] != suit:
            return hand, 0

    ordered = ([c[1] for c in hand]).sort

    if ordered[0] == 10:
        return [], 100_000_000
    return hand, 0

def StraightFlush(hand):
    ordered = ([c[1] for c in hand]).sort

    first = ordered[0]
    
    for i in range(1,ordered):
        if ordered[i] + i != first:
            return hand, 0
        
    return [], 6705994*ordered[len(ordered)-1]

def  equalCards(hand):
    equal = {}

    for i in range(len(hand)):
        if not equal.__contains__(hand[i][1]):
            equal[hand[i][1]] = 1
            
        else:
            equal[hand[i][1]] += 1

    count = 0
    card = 0
    for c in equal.keys():
        if equal[c] >= count and c>card:
            count = equal[c]
            card = c


    indexToRemove = []
    


    for i in range(len(indexToRemove.sort(reverse=False))):
        hand.remove(i)
    
    # match count:
    #     case 1:
    #     case 2:
    #     case 3:
    #     case 4:
    # return hand, 




        


PokerHand()
