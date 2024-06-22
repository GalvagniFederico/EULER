from collections import Counter

# 0 High Card: Highest value card.
# 1 One Pair: Two cards of the same value.
# 2 Two Pairs: Two different pairs.
# 3 Three of a Kind: Three cards of the same value.
# 4 Straight: All cards are consecutive values.
# 5 Flush: All cards of the same suit.
# 6 Full House: Three of a kind and a pair.
# 7 Four of a Kind: Four cards of the same value.
# 8 Straight Flush: All cards are consecutive values of same suit.
# 9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# Map ranks to value
values = {r: i for i, r in enumerate("23456789TJQKA", 2)}
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]
straights = [(v,v-1,v-2,v-3,v-4) for v in range(14,5,-1)] + [(14,5,4,3,2)]



def HandScore(hand):
    # Count cards of the same rank and get ranks
    a = list(Counter(x[0] for x in hand).items())
    score = list(zip(*sorted(((v, values[k]) for k, v in Counter(x[0] for x in hand).items()), reverse=True)))
    
    a = [1,2,3]
    b = ["a", "b", "c"]
    b = list(zip(a,b))
    score[0] = ranks.index(score[0])

    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5  # Flush

    if tuple(score[1]) in straights:
        score[0] = 8 if score[0] == 5 else 4

    return score

def Solve():
    hands = (line.split() for line in open('054_poker\\file.txt'))
    
    p1 = 0
    
    for hand in hands:
        if HandScore(hand[:5]) > HandScore(hand[5:]):
            p1+=1

    print(p1)


Solve() 


