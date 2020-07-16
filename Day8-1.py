a,b=map(int,input('Enter dividend and divisor:').split())
res=0
t=0
for i in range(31,-1,-1):
    if(t+(b<<i)<=a):
        t+=b<<i
        res|=1<<i
print(res)
