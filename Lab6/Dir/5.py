n = int(input())
some_list = []
for i in range(n):
    item = input()
    some_list.append(item)
file = open("test.txt", "w")
for item in some_list:
    file.write(item)
file.close()