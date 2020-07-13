#Day9-1 Aishwarya & Puper
n=int(input())
s=[int(x) for x in input().split()]
for i in range(int(input())):
    l,r=map(int,input().split())
    l1=s[l-1:r]
    c=0
    f=l1[0]
    if l1[0]==0:
            c+=1
    for j in range(1,len(l1)):
        #print(i,end='--')
        x=l1[j]
        if x==0:
            c+=1
        f^=x
        #print(f,c)
    print(f,c)
        
