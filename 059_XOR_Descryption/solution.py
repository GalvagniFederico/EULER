from itertools import product

def Encrypt(text, key):
    res = []
    
    for i in range(len(text)):
        res.append(text[i] ^ key[(int(i%(len(key)-1)))])

    return res
def Decrypt(text, key):
    res = []
    a = key[0]

    for i in range(len(text)):
        res.append(bool(text[i]) != bool(key[(int(i%(len(key)-1)))]))

    return res 

def Solve():
    t= ""
    for line in open("059_XOR_Descryption\encrypted.txt"):
        t += line

    a = (0,0,0)
    b = a[0]
    rawAscii = [int(i) for i in  t.split(",")]

    # rawAscii = [ord(c) for c in "s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."]
    # rawAscii = Encrypt(rawAscii, [ord(c) for c in "key"])

        
    keyCodes = list(product([i for i in range(97,122)], repeat = 3))
    
    bestCandidateText = ""
    bestCandidateScore = 0
    bestCandidateKeyCode = ""

    for key in keyCodes:
        isCandidate = True
        candidateText = ""
        candidateScore = 0

        for i in range(len(rawAscii)):
            encryptionKey = key[(int(i%(len(key)-1)))]

            decryptedAscii = rawAscii[i] ^ encryptionKey


            # if (decryptedAscii >= 35 and decryptedAscii <= 38) or decryptedAscii > 122 or decryptedAscii == 64 or decryptedAscii == 94 or decryptedAscii == 95:
            #     isCandidate = False
            #     break

            
#            if (decryptedAscii >= 65 and decryptedAscii <= 122)

            # Assign score to candidate
            # A-Z or a-z 100 points
            if decryptedAscii >= 65 and decryptedAscii <= 122:
                candidateScore += 100
                
            # Space 7
            if decryptedAscii == 32:
                candidateScore += 7

            # Punctuation 3
            if decryptedAscii == 33 or decryptedAscii == 34 or decryptedAscii == 46 or decryptedAscii == 44 or decryptedAscii == 63:
                candidateScore += 1

    
            candidateText += chr(decryptedAscii)

        if isCandidate and candidateScore > bestCandidateScore:
            bestCandidateKeyCode = ''.join(chr(i) for i in key)
            bestCandidateText = candidateText
            bestCandidateScore = candidateScore

    return bestCandidateText

print(Solve())
