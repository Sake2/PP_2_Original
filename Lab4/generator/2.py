def even(N):
    i = 0
    while (i <= N):
        if (i % 2 == 0):
            yield i
        i+=1
N = int(input())
for i in list(even(N)):
    print(i,end = " ")
        