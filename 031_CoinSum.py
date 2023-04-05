import time
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
def CoinSum(n):
    result = 0
    count = 0
    start_time = time.time()
    for p200 in range(0,n+1, 200):
        if(p200 > n):break
        for p100 in range(0,n+1,100):
            if(p200+p100 > n): break
            
            for p50 in range(0,n+1,50):
                if(p200+p100+p50 > n): break

                for p20 in range(0,n+1, 20):
                    if(p200+p100+p50+p20 > n): break
                    for p10 in range(0,n+1, 10):
                        if(p200+p100+p50+p20+p10 > n): break

                        for p5 in range(0,n+1,5):
                            sum = p200+p100+p50+p20+p10+p5
                            if(sum > n): break
                            r = n-sum
                            resto = r%2
                            if(resto==0):
                                result += (r)//2 + 1
                            else:
                                result += (r)//2 + resto
                            # for p2 in range(0,n+1,2):
                            #     if(sum+p2 > n): break
                            #     result += 1
                                
    print("Process finished --- %s seconds ---" % (time.time() - start_time)) 
                                      
    print(result)

    
            

CoinSum(10000)