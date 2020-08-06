def func2(a,n,k,c):
    if k==len(a):
        return c
    if a[k]==n:
        c+=1
    return func2(a,n,k+1,c)


a=[int(x) for x in input('Enter list of numbers seperated by space:').split()]
n=int(input('Enter the no. to search:'))
print(func2(a,n,0,0))
