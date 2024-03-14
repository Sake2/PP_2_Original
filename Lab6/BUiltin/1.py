def product(some_list) :
    prod = 1
    for i in range (len(some_list)):
        prod *= some_list[i]
    return prod
some_list = [1,2,3,4,5,6,7,8]
print(product(some_list))
        
    
