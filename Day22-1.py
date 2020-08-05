def func1(a,k):
    if k==len(a):
        return a
    if a[k]<0:
        a[k]=0
    return func1(a,k+1)
    

a=[int(x) for x in input('Enter the numberes seperated by space:').split()]
print(func1(a,0))
