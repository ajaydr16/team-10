def fun(n):
    return bin(n).replace('0b','').count('1')
for j in range(int(input())):
    n=int(input())
    flag=False
    for i in range(1,n):
    #print(i,fun(i))
        if (i+fun(i))==n:
        #print(fun(i))
        #print(i)
            flag=True
            break
    if flag:
        print(0)
    else:
        print(1)
    
    
