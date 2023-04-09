

def isTriangular(n):
    i = 0
    while True: 
        th = ((0.5*i)*(i+1))
        if th == n:
            return True
        if th > n: 
            return False
        i+=1

def WordValue(w):
    result = 0
    for char in w:
        result += ord(char) - ord("A") + 1
    return result

#print(WordValue("SKY"))

def CodedTriangulraNumber():
    words = open("file/042_TriangularNames.txt", "r")
    s = words.read()
    n = s.replace("\"", "").split(",")
    print(n)

    word_values = []
    
    for i in range(0,len(n)):
        word_values.append(WordValue(n[i]))

    result = 0

    for i in range(0, len(word_values)):
        if isTriangular(word_values[i]):
            result+=1
    return result

print(CodedTriangulraNumber())