import math
import time
def Division(n):
    resto = -1
    risultato = []
    d = 1
    while len(risultato)<= n*3:
        if(d<n):
            d = d*10
            risultato.append(0)
        else:
            risultato.append(d//n)
            d = d%n
            d *= 10
            if(d == 0):
                return(risultato[1:])

    return risultato[1:]

#print(Division(992))

def FindPeriod(n):
    n = Division(n)
    index = 0
    l = 1

    while True:
        if(index>= len(n)-1):
            return []
        period = n[index:index +l]
        b = True
        for i in range(index + l,math.floor(len(n))-l,l):
            temp = n[i:i+l]
            if(not n[i:i+l] == period):
                l += 1
                b= False
                break

        if  index + l*2 >= (len(n)):
            l = 1
            b= False
            index += 1

        if(b == True):
            return period

#print(len(FindPeriod(887)))

#MR RIP SOLUTION 100X FASTER
def RecurringCycle(n):
    
    d = {}
    start = 1
    while True:
        while start<n:
            start = start*10
            
        start = start%n
        if(start == 0): 
            return 0

        if start in d.keys():
            return len(d.keys())
        d[start] = True
    

#print(RecurringCycle(36))


def ReciprocalCycles(n):
    start_time = time.time()
    result = 0
    max = 0
    for i in range(2,n):


        lenght = RecurringCycle(i)
        if(lenght > max):
            max = lenght
            result = i
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    
    return result

print(ReciprocalCycles(1001))

