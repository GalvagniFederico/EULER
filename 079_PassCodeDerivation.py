# A common security method used for online banking is to ask the user for three random 
# characters from a passcode. For example, if the passcode was 531278, they may ask 
# for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as to
# determine the shortest possible secret passcode of unknown length.

def PassCodeDerivation():
    attempts = [str(int(line)) for line in open("file/079_Attempts.txt", "r").readlines()]
    res = ""
    previousDigitsOfDigits = {}

    for i in range(len(attempts)):
        for j in range(0,len(attempts[i])):

            if attempts[i][j] not in previousDigitsOfDigits.keys():
                previousDigitsOfDigits[attempts[i][j]] = []

            if j > 0: 
                previousDigitsOfDigits[attempts[i][j]] = [attempts[i][j-1]]

    # Found digits with no predecessor (it's the next digits of the passcode), then remove
    # this digits from all the previous digits record
    # Repeat the process until all unique digits are processed
    while len(previousDigitsOfDigits) > 0:
        nextLetter = ""
        for  k in previousDigitsOfDigits.keys():
            if len(previousDigitsOfDigits[k]) == 0: 
                previousDigitsOfDigits.pop(k)
                nextLetter = k
                res += k
                break
                
        # Remove new letter
        for k in previousDigitsOfDigits.keys():
            previousDigitsOfDigits[k] = [item for item in previousDigitsOfDigits[k] if item != nextLetter]

    return res

print(PassCodeDerivation())

# 73196280