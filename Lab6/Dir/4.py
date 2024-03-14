file = input()
filename = open(file,"r")
count = 0
for line in filename.readlines():
    count +=1
print(count)