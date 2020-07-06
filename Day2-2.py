l=[int(x) for x in input().split()]
m2,m=l[0],l[0]
for i in range(len(l)):
        m=max(l[i],m+l[i])
        m2=max(m2,m)
        
print("Sum is:",m2)
