#Power of 2 or not
n=int(input())
if n and(not(n& (n-1))):
    print('YES')
else:
    print('NO')

