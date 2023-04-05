def NamesSores():
    f = open("file/021_NamesScores.txt")
    s = f.read()
    n = s.replace("\"", "").split(",")
    n.sort()
    result = 0
    for i in range(len(n)):
        result += NameRank(n[i])*(i+1)
    return result

def NameRank(str:str):
    score = 0
    for c in str.lower():
        score += ord(c)-ord("a")+1
    return score

#print(NameRank("coLin"))
print(NamesSores())