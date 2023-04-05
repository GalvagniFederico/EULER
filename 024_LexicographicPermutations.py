import math

def LexicographicPermutations(set:list, pos):
    pos = pos-1
    result = []
    while len(set) !=0:
        combinazioni = int(math.factorial(len(set)-1))
        indice = pos//combinazioni
        resto = pos%combinazioni
        result.append(set[indice])
        set.remove(set[indice])
        pos = resto
    return result

        
    


print(LexicographicPermutations([0,1,2,3,4,5,6,7,8,9], 1000000))