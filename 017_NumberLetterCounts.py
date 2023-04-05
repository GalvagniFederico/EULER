unit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decimal = ["","","twenty", "thirty", "forty", "fifty","sixty", "seventy", "eighty", "ninety"]
bo = ["hundred", "thousand"]

def NumberToLetters(n):
    n = str(n)
    nl = ""
    
    b = False
    for i in range(len(n)-1,-1,-1):
        
        #UNIT + TEEN
        if(len(n)>0 and i >= len(n)-2):
            
            t = int(n[len(n)-2:len(n)])
            if(t)<20 and not b:
                if(n[i]!= "" and n[i-1] != "" and len(n)>2 and t >0):
                    nl = nl +"and"+ unit[t]
                else:  
                    nl = nl + unit[t]
                b = True
                continue
            else:
                #UNIT IF N < 10
                if(i==len(n)-1 and not b):
                    d = int(n[i])
                    nl = nl + unit[int(n[i])]

                #DECIMAL
                if(i == len(n)-2 and not b):
                    if(n[i+1]) != "" and n[i] != "" and len(n)>2:
                        nl ="and"+ decimal[int(n[i])] + nl
                    else:
                        nl = decimal[int(n[i])] + nl
        
        if(i <= len(n)-3):
            u = unit[int(n[i])]
            if(u != ""):
                nl = unit[int(n[i])] + bo[len(n)-i-3] + nl
            
    return nl
#print(NumberToLetters(500))

def NumberLetterCount():
    result = 0
    for i in range(1,1001):
        print(i, NumberToLetters(i), len(NumberToLetters(i)))
        result += len(NumberToLetters(i))
        
    return result

print(NumberLetterCount())
