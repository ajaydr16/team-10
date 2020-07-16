a,b=map(int,input().split())
res=0
while b>0:
    if b&1:
        res+=a
    a=a<<1
    b=b>>1
print(res)
    
