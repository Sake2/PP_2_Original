def square(N):
    i = 1
    while (i <= N):
        yield i * i
        i+=1
N = int(input())
a =list(square(N))
print(a)