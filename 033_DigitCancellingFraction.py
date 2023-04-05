
def isCancellingFraction(n,d):
    if(str(n)[0] == str(n)[1] or str(d)[0] == str(d)[1] or str(n)[1] != str(d)[0]): return False
    cd = str(d)[1]
    cn = str(n)[0]

    if cn != "0" and cd != "0":
        if(n/d == int(cn)/int(cd)): return True
        else: return False
def LowestCommonTerms(arr):
    bigger = 0
    for d in arr:
        if(d[1]>bigger):
            bigger = d[1]
    
    max_den = bigger
    while True:
        found = True
        for d in arr:
            if(max_den%d[1] != 0):
                found = False
                break
        if found:

            break
        max_den +=bigger
    
    den = 0
    for i in range(len(arr)):
        den += max_den/arr[i][1] * arr[i][0]
    return den

                
def MultiplyFraction(arr:list):
    result = [1,1]
    for i in range(len(arr)):
        result[0] *= arr[i][0]
        result[1] *= arr[i][1]
    return result

def LowestCommonTerms(arr:list):
    div = min(arr)
    while True:
        if(arr[1]%div == 0 and arr[0]%div == 0):
            return [arr[0]//div, arr[1]//div]
        div -=1

def DigitCancellingFraction():
    arr = []
    for i in range(10, 100):
        for j in range(i, 100):
            if(isCancellingFraction(i,j)):
                arr.append([i,j])

    return LowestCommonTerms(MultiplyFraction(arr))[1]


    #return LowestCommonTerms(arr)
    


#print(isCancellingFraction(49,99))
print(DigitCancellingFraction())