def rev_sen(strr) :
    _list = strr.split()
    list1 = _list[ ::-1]
    list1 = (" ".join(list1))
    return list1

strr  = input()
print(rev_sen(strr))
