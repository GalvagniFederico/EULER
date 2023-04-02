import math
def ChampernownesConstant(th):
    if th <= 9:
        return th
 
    minus = [0]
    result = ""

    for i in range(1, len(str(th))+1):
        t = 0
        if i > 0:
            for j in range(0,i):
                
                t += minus[j]
        else:
            t =1

        minus.append(i*math.pow(10,i)-t - i)
    minus[1] = 10
    num = 0
    for i in range(len(minus)-1, 0,-1):
        if th-minus[i]>=0:
            th -= minus[i]
            iChar = 0
            #num = 0
            # if th < i:
            #     num = (1*math.pow(10, i-1) + math.floor(th/i))
            #     iChar = th
            # else:
            
            if th < i:
                num = (1*math.pow(10,i))-1
                iChar = th
            else:
                num = (1*math.pow(10, i) + math.floor(th/i))
                iChar = th % i

            result = str(num)

            
            if iChar < 0:
                iChar *= -1
            
            return result[int(iChar)]
            

# 01234567891011
print(ChampernownesConstant(12))

def ChampernownesConstant__UnitTest():
    res = []
    for i in range(0, 100):
        s = str(i)
        for i in  range(0, len(s)):
            res.append(s[i])
    
    for i in range(12, len(res)):
        t = ChampernownesConstant(i)
        if str(t) != str(res[i]):
            
            for j in range(0, len(res)):
                print(j, res[j])
            return "Test Failed! Index: " + str(i)
        


    return "Test Passed"

#print(ChampernownesConstant__UnitTest())