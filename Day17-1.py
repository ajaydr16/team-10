def fun(w,i,b):
    l=[]
    for j in range(len(b)):
        if w[i] in b[j]:
         if b[j].count(w[i])>1:
            
            for k in range(len(b[j])):
                if b[j][k]==w[i]:
                    l.append(str(j)+str(k))
         l.append(str(j)+str(b[j].index(w[i])))
    return l

def check(w,k,l,c,d):
    p1,p2=int(k[0]),int(k[1])
    #print('s')
    if p1-1>=0:
        
        if l[p1-1][p2]==w[c] and str(p1-1)+str(p2) not in d:
                #print('1')
                c=c+1
                k=str(p1-1)+str(p2)
                d.append(k)
                #print(c)
                return k
    if p1+1<len(l):
        
        if l[p1+1][p2]==w[c] and str(p1+1)+str(p2) not in d:
                #print('2')
                c+=1
                k=str(p1+1)+str(p2)
                d.append(k)
                #print(c)
                return k
    if p2-1>=0:
        
        if l[p1][p2-1]==w[c] and str(p1)+str(p2-1) not in d:
                #print('3')
                c+=1
                k=str(p1)+str(p2-1)
                d.append(k)
                #print(c)
                return k
    if p2+1<len(l[0]):
        
        if l[p1][p2+1]==w[c] and str(p1)+str(p2+1) not in d:
            #print('4')
            c+=1
            k=str(p1)+str(p2+1)
            d.append(k)
            #print(c)
            return k
    return k
    
m1,m2=map(int,input('Enter the row count and column count:').split())
b=[]
for i in range(m1):
    b1=[x for x in input().split()]
    b.append(b1)

w=input('Enter the word:')
n=len(w)
c=1
k=0
i=0
d=[]
l=fun(w,0,b)
for j in range(len(l)):
    k=l[j]
    #d.append(k)
    #lst=list(check(w,k,b,c))
    #d=[]
    #print('hello')
    for q in range(1,len(w)):
        p= check(w,k,b,q,d)
        k=p
        #if len(d)>=n-2 and b[int(d[-1][0])][int(d[-1][1])]==w[-1]:
        #   break
        #print(d)
#print(d)
#print(c)

if len(d)>0 and b[int(d[-1][0])][int(d[-1][1])]==w[-1]: 
     print('True')
else:
    print('False')
        
                    
                
