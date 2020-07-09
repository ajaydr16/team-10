l=[int(x) for x in input('Enter the array of integers sepearated by space:').split()]
l.sort()
for i in range(0,len(l)-1,2):
    if l[i]^l[i+1]:
        print(l[i])
        break

