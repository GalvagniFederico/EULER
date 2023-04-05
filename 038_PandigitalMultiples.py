def isPandigital(s):
    test = [str(c) for c in s]
    test.sort()
    if test == ["1", "2", "3", "4","5", "6","7", "8", "9"]:
        return True
    return False





def PandigitalMultiples():
    limit = 9999
    number = 1
    result = 0
    result_number = 0
    while number <= limit:
        m_limit = 9//len(str(number))
        m=  1

        concatened_products = ""
        while m <= m_limit:
            product = str(m*number)
            if len(concatened_products)+len(product) > 9:
                m+=1
                continue
            else:
                concatened_products += product
                m+=1

        if(len(concatened_products) != 9):
            number+= 1
            continue

        if(isPandigital(concatened_products)):
            if int(concatened_products) > result:
                result = int(concatened_products)
                result_number = number
        number += 1
    return result, result_number



                



        


print(PandigitalMultiples())
