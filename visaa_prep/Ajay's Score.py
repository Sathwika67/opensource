t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    total=x//10
    score=total*n
    print(score)
