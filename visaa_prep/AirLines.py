x,n=map(int,input().split())
planes=n//100
total_planes=planes-x
if n%100==0:
    purchase=total_planes
else:
    purchase=total_planes+1
print(purchase)
    
    
    
