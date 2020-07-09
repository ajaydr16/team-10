A=int(input())
c=0
for i in range(1,A+1):
    c=(c+bin(i).replace('0b','').count('1'))%((10**9)+7)
print('count:',c)
