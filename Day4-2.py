A=[int(x) for x in input('Enter the array of n integers with space seperated:').split()]
s1,s2=max(A),max(A)
value=max(A)
for i in range(len(A)):
    s=A[i]
    for j in range(len(A)):
        if i==j:
            continue
        elif s^A[j]<value:
            s1=s
            s2=A[j]
            value=s^A[j]
print('The pair is:('+str(s1)+','+str(s2)+') with XOR value='+str(value))

        
        
