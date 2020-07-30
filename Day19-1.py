s=input()
m,c,i,d=0,0,0,[]
while i<len(s):
    if s[i] not in d:
            c+=1
            d.append(s[i])
    else:
        d=[]
        c=0
    m=max(c,m)
    i+=1
print(m)
    
