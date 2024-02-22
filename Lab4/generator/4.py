import math
def square(a,b):
    i = a
    while(i <= b):
        yield i * i
        i+=1
a = int(input())
b = int(input())
for i in list(square(a,b)):
    if (math.sqrt(i) == int(math.sqrt(i))):
        print(i ,end = " ")