import math
import time

def SpecialPythagoreanTriplet(n):
    start_time = time.time()
    for i in range(1,n):
        for j in range(i+1, n-i+1):
            for k in range(j+1, n-j-i+1):

                i2 = i**2
                j2 = j**2
                k2 = k**2
                
                if(i2+j2==k2):
                    
                    if(i+j+k == n):
                        print("Process finished --- %s seconds ---" % (time.time() - start_time))
                        print("YO we found it")
                        print(i,j,k)
                        print(i*j*k)
                        return

    

print(SpecialPythagoreanTriplet(1000))