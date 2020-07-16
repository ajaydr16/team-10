#Day12-2
for j in range(int(input())):
    n=int(input())
    b=bin(n).replace('0b','')
    b='0'*(8-len(b))+b
    s=''    
    for i in range(len(b)):
        if i%2==0:
            if (i+1)<len(b):
             s+=b[i+1]
        else:
                s+=b[i-1]

    #print(s,b,end='-')
#print()
#print(s)
    print(int(''.join(s),2))
        
