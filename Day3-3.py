#Day3-3: Check if the ith bit is set in the binary form of the given number.
n=bin(int(input('Enter the binary number:'))).replace('0b','')
i=int(input('Enter the ith position:'))
#print(n)
if n[i-1]=='1':
    print('SET BIT')
else:
    print('Not a SET BIT')
