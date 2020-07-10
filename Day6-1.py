n=int(input())
k=1
d={}
i=1
while k<=n:
    s=bin(i).replace('0b','')
    #print(s)
    if s==s[-1::-1]:
        d[k]=s
        k+=1
    i+=1
print(int(d[n],2),d[n])
#print(d)

    
    

