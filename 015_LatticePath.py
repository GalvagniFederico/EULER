import time
import math
def CleanStack(stack:list):
        toRemove = 0
        
        for i in range(len(stack)-1, -1,-1):
            if stack[i][2] == 2:
                toRemove += 1
            else:
                return stack[0:len(stack) - toRemove], i
        return stack[0:len(stack) - toRemove], 0

# start_time = time.time()

# for i in range(200000):
#     CleanStack([[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 2], [4, 1, 1], [5, 1, 2], [5, 2, 1], [6, 2, 1], [7, 2, 2], [7, 3, 1], [8, 3, 2], [8, 4, 2], [8, 5, 1], [9, 5, 2], [9, 6, 1], [10, 6, 2], [10, 7, 
# 2], [10, 8, 2], [10, 9, 2], [10, 10, 2]])
# print("Process finished --- %s seconds ---" % (time.time() - start_time))



def LatticePath(n):
    # STACK DEVE ASSOLUTMANTE ESSERE UNA MATRICE O UN DICTIONARY

    start_time = time.time()
    x,y = 0, 0
    count = 0
    stack_i = 0
    cycle = 0
    stack =  []
    stack.append([x,y,0])

    while True:
        cycle+=1
        match stack[stack_i][2]:
            case 0:
                # RIGHT
                stack[stack_i][2] = 1
                if(x<n):
                    x+=1
                    stack_i+=1
                    stack.append([x,y,0])
                    
            case 1:
                # DOWN
                stack[stack_i][2] = 2

                if(y<n):
                    y+=1
                    stack_i+=1
                    stack.append([x,y,0])
                # could clean stack here
            case 2:
                stack, stack_i = CleanStack(stack)

                if(len(stack) == 0): 
                    print("Process finished --- %s seconds ---" % (time.time() - start_time))
                    print("Cycle: " + str(cycle))
                    return count

                x = stack[stack_i][0]
                y = stack[stack_i][1]

        if(x == n and y == n):
            count+=1
            stack[stack_i][2] = 2
            stack, stack_i = CleanStack(stack)
            #posso vedere se stack[i][2] è vuoto e ritornare
            if(len(stack) == 0): 
                print("Process finished --- %s seconds ---" % (time.time() - start_time))
                return count


            x = stack[stack_i][0]
            y = stack[stack_i][1]

            
#print(LatticePath(20))

def LatticePath2(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    


print(LatticePath2(40, 20))
