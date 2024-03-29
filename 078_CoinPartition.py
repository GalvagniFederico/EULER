import math

def pentagonal(n):
    result = (n * ((3*n)-1))/2
    return int(result)

def division(n):
    res = 0
    for i in range(n, 1, -1):
        if n%i == 0:
            res+=1
        elif (n%i)%1==0:
            res+=1

# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7)
# 5 7 12 15 22 sequenza generalizzata pentagonal number ottenuta da (n*((3*n)-1))/2 chiamata in sequenza 0 1 -1 2 -2 3 -3 ....
def partition():
    p_mem = {0:1,
             1:1,
             2: 2}
             
    res = 0
    n = 3

    pentagonals = {}
    while p_mem[n-1]%1000000 != 0:
        # creo tutti i numeri pentagonali fino a n
        for n_i in range(3,n+1):

            # First I sum p(n-1) + p(n-2) then i subtract p(n-gpns) gp: generalized pentagonal number sequence
            p_n = p_mem[n_i-1] +p_mem[n_i-2]

            iPentagonal = 2

            while True:
                if not pentagonals.__contains__(iPentagonal):

                    pentagonals[iPentagonal]= pentagonal(iPentagonal)
                if n_i - pentagonals[iPentagonal] < 0:
                    break


                if iPentagonal%2==0:
                    p_n -= p_mem[n_i - pentagonals[iPentagonal]]
                else:
                    p_n += p_mem[n_i - pentagonals[iPentagonal]]

                if iPentagonal < 0:
                    iPentagonal *= -1
                    iPentagonal += 1

                else:
                    iPentagonal *= -1
    
            p_mem[n_i] = p_n
            
        
        print(str(n) + " - " + str(p_mem[n]))
        
        n+=1
        
    print(n)

#partition()


# Found out that p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7)
# 1 2 5 7 12 ... is the generalized pentagonal number sequence
# The sequence above can be generated by feeding a sequence (1, -1, 2, -2, 3, -3, ...) 
# to the formula  (n * ((3*n)-1))/2
def partition2():
    pentagonals = [1,2]
    partitions = [1,1]
       
    lastpartition = 1
    n = 2 

    while lastpartition%1000000!=0:
        lastpartition = 1
        pentagonals.append(pentagonal(n))
        pentagonals.append(pentagonal(-n))
        lastpartition = 0



        i = 0
        while n - pentagonals[i] >= 0:
            diff = n-pentagonals[i]   
            tr = partitions[diff]
            if math.floor((i+2)/2) % 2 == 1:    
                lastpartition += partitions[n-pentagonals[i]]
            else:
                lastpartition -= partitions[n-pentagonals[i]]
            i+=1
        partitions.append(lastpartition)
        n+=1

    return n-1
            

        


print(partition2())


    # 3 - 3
    # OOO
    # OO O
    # O O O

    # 4 - 5
    # OOOO
    # OOO O
    # OO OO
    # OO O O
    # O O O O

    # 5 - 7
    # OOOOO
    # OOOO   O
    # OOO   OO
    # OOO   O   O
    # OO   OO   O
    # OO   O   O   O
    # O   O   O   O   O

    # 6 - 11
    # OOOOOO
    # OOOOO O
    # OOOO OO
    # OOOO O O
    # OOO OOO
    # OOO OO O
    # OOO O O O
    # O0 0000
    # 00 00 00
    # 00 00 0 0
    # 00 0 0 0 0
    # 0 0 0 0 0 0

    # 7 
    # OOOOOOO
    # 0 000000
    # 00 00000
    # 000 0000
    # 0 00000
    #
    #
    #