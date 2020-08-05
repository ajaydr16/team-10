def func2(a,k):
        if k<=0:
            return True
        if a[len(a)-k]!=a[k-1]:
            return False
        return func2(a,k-1)
a=[int(x) for x in input('Enter list of numbers seperated by space:').split()]
print(func2(a,len(a)))
