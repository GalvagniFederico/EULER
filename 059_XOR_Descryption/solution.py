from itertools import product
from decimal import Decimal
import time
import sys



last_print = time.time()
aloa = "aaa"



def percent_complete(step, total_steps, start_time, bar_width=60, title="",  print_perc=True, print_time=True):
    # global last_print
    # me = last_print
    # if time.time() - me > 0.1 and step != total_steps:
    #     last_print = time.time()
    # else:
    #     return

    # UTF-8 left blocks: 1, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8
    utf_8s = ["█", "▏", "▎", "▍", "▌", "▋", "▊", "█"]
    perc = 100 * float(step) / float(total_steps)
    max_ticks = bar_width * 8
    num_ticks = int(round(perc / 100 * max_ticks))
    full_ticks = num_ticks / 8      # Number of full blocks
    part_ticks = num_ticks % 8      # Size of partial block (array index)
    
    disp = bar = ""                 # Blank out variables
    bar += utf_8s[0] * int(full_ticks)  # Add full blocks into Progress Bar
    
    # If part_ticks is zero, then no partial block, else append part char
    if part_ticks > 0:
        bar += utf_8s[part_ticks]
    
    # Pad Progress Bar with fill character
    bar += "▒" * int((max_ticks/8 - float(num_ticks)/8.0))
    
    if len(title) > 0:
        disp = title + ": "         # Optional title to progress display
    
    # Print progress bar in green: https://stackoverflow.com/a/21786287/6929343
    disp += "\x1b[0;32m"            # Color Green
    disp += bar                     # Progress bar to progress display
    disp += "\x1b[0m"               # Color Reset
    if print_perc:
        # If requested, append percentage complete to progress display
        if perc > 100.0:
            perc = 100.0            # Fix "100.04 %" rounding error
        disp += " {:6.2f}".format(perc) + " %"

    if print_time:
        disp += "  eta: " + '{0:02.0f}:{1:02.0f}'.format(*divmod((time.time()-start_time) * 60, 60))
      

    # Output to terminal repetitively over the same line using '\r'.
    sys.stdout.write("\r" + disp)
    sys.stdout.flush()


def Encrypt(text, key):
    res = []
    
    for i in range(len(text)):
        res.append(text[i] ^ key[(int(i%(len(key))))])

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

    customKey = "abcde"

    
    text = "Possiamo provare con qualcosa a caso inventato al momento cryptato con una chiave a nostra scelta e la soluzione avverrebbe comuqnue con successo"
    text = Encrypt([ord(i) for i in text], [ord(i) for i in customKey])
    rawAscii = text
    
    # rawAscii = [int(i) for i in  t.split(",")]
    keyCodes = list(product([i for i in range(97,122)], repeat = len(customKey)))


    bestCandidateText = ""
    bestCandidateScore = 0
    bestCandidateRowAscii = 0

    l=0
    prev_l = 0
    l_span = 10

    start_time = time.time()

    badValue = [[] for i in range(len(customKey))]

    for key in keyCodes:
        isCandidate = True
        candidateText = ""
        candidateScore = 0
        candidateRowAscii = []

        skip = False

        for i in range(len(key)):
            if badValue[i].__contains__(key[i]):
                skip = True

        if skip:
            continue

        if l - prev_l >= l_span:
            percent_complete(l, len(keyCodes),start_time)
            prev_l = l

        l+= 1
        

        for i in range(len(rawAscii)):
            definetlyWrong=False
            encryptionKey = key[(int(i%(len(key))))]
            decryptedAscii = rawAscii[i] ^ encryptionKey


            candidateText += chr(decryptedAscii)
            candidateRowAscii.append(decryptedAscii)

            # if (decryptedAscii >= 32 and decryptedAscii <= 125) or decryptedAscii == 232 or decryptedAscii == 127:
            #     candidateScore += 1
            # else:
            #     candidateScore -= 1000
            
            if (decryptedAscii >= 97 and decryptedAscii <= 122) or (decryptedAscii >= 65 and decryptedAscii <= 90) or decryptedAscii == 32 :
                candidateScore += 100
            elif decryptedAscii > 125 or decryptedAscii < 30:
                badValue[int(i%len(key))].append(encryptionKey)
                definetlyWrong = True
                candidateScore -= 1000
            else:
                candidateScore-= 500

            if candidateScore < 0:
                break

        if isCandidate and candidateScore > bestCandidateScore:
            bestCandidateKeyCode = ''.join(chr(i) for i in key)
            bestCandidateText = candidateText
            bestCandidateScore = candidateScore
            bestCandidateRowAscii = sum(candidateRowAscii)
        
        if definetlyWrong:
            continue
    percent_complete(1, 1, start_time)
    return bestCandidateRowAscii, bestCandidateKeyCode, bestCandidateText, "".join([chr(i) for i in Encrypt([ord(i) for i in bestCandidateText], [ord(i) for i in bestCandidateKeyCode])]), bestCandidateScore


result = Solve()
print("\n Result: ",result[0], " with key code \"", result[1], " - score: ", result[4], "\n\n Encrypted Text:", result[3], "\"\n\n Text: \n ", result[2])
