def div3_4(N):
    i = 0
    while(i <= N):
        if (i % 4 == 0 and i % 3 == 0):
            yield i
        i+=1
N =int(input())
print(list(div3_4(N)))