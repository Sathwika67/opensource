t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if m>n or n==m:
        print("0")
    else:
        print(n-m)
        
