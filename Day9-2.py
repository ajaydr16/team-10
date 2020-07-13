#Day9-2
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=0
    l.sort()
    min=l[0]
    for j in range(len(l)):
        f=l[j]
        for k in range(len(l)):
            if k==j:
                continue
            else:
                temp=f^l[k]
                if temp<min:
                    min=temp
           
            
    print(min)

        
