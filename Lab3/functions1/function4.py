x = [i for i in range(100)]
def filter_prime(_list) :
    list1 = []
    for i in range(len(_list)) :
        list1.append(_list[i])
        for j in range(2,int(_list[i]**0.5)+1):
            if _list[i] % j == 0  or _list[i] < 1:
                list1.pop(-1)
                break
    return list1
print(filter_prime(x))
        