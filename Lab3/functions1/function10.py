def unique_elements(_list):
    unique_list = []
    for i in _list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

_list = [1, 2, 3, 3, 4, 5, 5, 6, 6]
result = unique_elements(_list)
print(_list)
print(result)
