n=int(input())
s=bin(n)
s=s[3:]+s[2]
print('SAFEST POSITION:',int(s,2))
