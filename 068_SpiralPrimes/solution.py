import sys
sys.path.insert(0, 'C:\\Users\\Federico\\Documents\\FEDERICO\\Other\\EULER')
import utilities
import time

def Solve():
    ratio = 1.0
    squareSize = 2
    squareStartingNumber = 1
    primeCount = 0

    start_time = time.time()
    while ratio >= 0.1:
        for i in range(1,4):
            if i == 4:
                continue

            corner = squareStartingNumber + i*squareSize
            
            if utilities.isPrime(corner):
                primeCount += 1
            
        ratio = primeCount/(((squareSize/2) *4) + 1)
        squareStartingNumber = squareStartingNumber+(squareSize*4) 
        squareSize += 2

    print(f"Process finished --- {time.time() - start_time} seconds ---")
    return squareSize-1

print(Solve())