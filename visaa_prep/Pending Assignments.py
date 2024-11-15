x,y,z=list(map(int,input().split()))
t=x*y
total_time=z*1440
if t<= total_time:
    print("YES")
else:
    print("NO")
