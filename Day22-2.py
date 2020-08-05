def func2(a,n,k):
    if k==len(a):
        return False
    if a[k]==n:
        return True
    return func2(a,n,k+1)


a=[int(x) for x in input('Enter list of numbers seperated by space:').split()]
n=int(input('Enter the no. to search:'))
print(func2(a,n,0))
