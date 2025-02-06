import math
import time
import cProfile

def gcd(n, f=2):
    divisor = []
    for i in range(math.floor(n/2)+1,f-1,-1):
        if n % i == 0:
            divisor.append(i)
    return divisor


def Totient(n):
    start_time = time.time()

    relPrimes = [set() for i in range(n+1)]

    for ni in range(len(relPrimes)):
        ii = math.floor(ni/2)+1

        while ii > 1:
            if ni%ii == 0:
                if len(relPrimes[ii])> 0:
                    relPrimes[ni].update(relPrimes[ii])
                    relPrimes[ni].add(ii)
                    for x in relPrimes[ii]:
                        di = 2
                        while True:
                            d = x*di
                            if ni < d:
                                if ni%d== 0:
                                    relPrimes[ni].add(d)
                                else:
                                    break
                            else:
                                break
                            di+=1
                    break
                else:
                    relPrimes[ni].add(ii)
            ii-=1
            
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

cProfile.run('Totient(10000)')