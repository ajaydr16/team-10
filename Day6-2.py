n=int(input())
b=(bin(n).replace('0b',''))
c=0
for i in range(len(b)-1,0,-1):
    if b[i]!='1':
        c+=1
    else:
        break
    
print(c)
