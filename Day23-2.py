def func2(a,k):
        if k==len(a)//2:
                return a
        temp=a[k]
        a[k]=a[len(a)-k-1]
        a[len(a)-k-1]=temp
        return func2(a,k+1)
a=[int(x) for x in input('Enter list of numbers seperated by space:').split()]
print(func2(a,0))
