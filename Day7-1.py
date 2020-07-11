#Day-7 Muffler Problem
def fun(p1,p2,l,d,c):
    if p1-1>=0:
        #print('1')
        if l[p1-1][p2]<18 or l[p1-1][p2]>50:
            if str(p1-1)+str(p2) not in d:
                d.append(str(p1-1)+str(p2))
                c=c+1
                
        
        if p2-1>=0:
             if l[p1-1][p2-1]<18 or l[p1-1][p2-1]>50:
                if str(p1-1)+str(p2-1) not in d:
                    d.append(str(p1-1)+str(p2-1))
                    c+=1
    
        if p2+1<len(l[0]):
             if l[p1-1][p2+1]<18 or l[p1-1][p2+1]>50:
                if str(p1-1)+str(p2+1) not in d:
                    d.append(str(p1-1)+str(p2+1))
                    c+=1
    if p1+1<len(l):
        #print('2')
        if l[p1+1][p2]<18 or l[p1+1][p2]>50:
            if str(p1+1)+str(p2) not in d:
                d.append(str(p1+1)+str(p2))
                c+=1
        if p2-1>=0:
         if l[p1+1][p2-1]<18 or l[p1+1][p2-1]>50:
         
                if str(p1+1)+str(p2-1) not in d:
                    d.append(str(p1+1)+str(p2-1))
                    c+=1
        if p2+1<len(l[0]):
            if l[p1+1][p2+1]<18 or l[p1+1][p2+1]>50:
         
                if str(p1+1)+str(p2+1) not in d:
                    d.append(str(p1+1)+str(p2+1))
                    c+=1
    if p2-1>=0:
        #print('3')
        if l[p1][p2-1]<18 or l[p1][p2-1]>50:
            if str(p1)+str(p2-1) not in d:
                d.append(str(p1)+str(p2-1))
                c+=1
    if p2+1<len(l[0]):
        #print('4')
        if l[p1][p2+1]<18 or l[p1][p2+1]>50:
            if str(p1)+str(p2+1) not in d:
                d.append(str(p1)+str(p2+1))
                c+=1
    return c

                                    
m,n=map(int,input().split())
l=[]
p1,p2=0,0
for i in range(m):
    l1=[int(x) for x in input().split()] 
    l.append(l1)
inf=int(input())
for i in range(m):
    if inf in l[i]:
        p1=i
        p2=l[i].index(inf)
        break
    
d=[]
d.append(str(p1)+str(p2))
#print(l[p1][p2])
c=0
#print(fun(p1,p2,l,d,c))
j=0
#print(d)
while j<len(d):
    ele=l[int(d[j][0])][int(d[j][1])]
    for i in range(m):
        if ele in l[i]:
            p1=i
            p2=l[i].index(ele)
            break
    c=fun(p1,p2,l,d,c)
    #print(j,d)
    j+=1
print('Total:',c)
#print(d)
    
