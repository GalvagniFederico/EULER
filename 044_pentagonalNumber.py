import math

def pentagonal(n):
    result = (n * ((3*n)-1))/2
    return result





def dPentagonal():
    p_set = set()
    p_list = []
    
    for i in range(1, 10000):
        p_list.append(int(pentagonal(i)))
        p_set.add(str(int(pentagonal(i))))

    print("Done")
    for i in range(0, len(p_list)):
        for j in range(i+1, len(p_list)):
            if (str(p_list[i] + p_list[j])) in p_set and (str(p_list[j] - p_list[i])) in p_set:
                print(str(p_list[i]) + " - " + str(p_list[j]))


dPentagonal()


    
    
