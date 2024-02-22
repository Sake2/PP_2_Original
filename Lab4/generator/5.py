def rev_range(N):
    i = N
    while( i >= 0):
        yield i
        i-=1
N = int(input())
for i in rev_range(N):
    print(i,end = " ")