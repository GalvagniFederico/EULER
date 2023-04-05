def CountingSundays(n):
    day = 2
    result = 0
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_i = 0
    year = 1901
    print("--- " + str(year) + " ---")
    while True:
        if(year%4==0):
            if(year%100 == 0):
                if(year%400 == 0):
                    month[1] = 29
            else:
                month[1] = 29
        else:
            month[1] = 28

        if(day+month[month_i]%7 > 7):
            day =  (month[month_i]%7) + day - 7
        else:
            day+=month[month_i]%7

                
        


        month_i+=1
        if(month_i == 12):
            
            year += 1
            month_i = 0
            print("--- " + str(year) + " ---")
            if(year > n): return result
        if(day == 1 and year < n):
            result+=1
            print(year, month_i+1)

print(CountingSundays(2000))
