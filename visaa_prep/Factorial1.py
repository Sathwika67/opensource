n=int(input())
def fact(n):
    if n<=0:
        result=1
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(fact(n))
