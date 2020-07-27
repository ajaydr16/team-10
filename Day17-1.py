'''
My Algorithm:
1. Taking Input
2. Finding the locations of the first charater of the given word input.Like if the word is 'ABCCE' then in the given
    2D array there are two places where letter 'A' is present. So first storing those locations.
3. Then iteratating through each loactions of that first character.
4. Then using a function I am iterating the 2D array to check the adjacent characters of that particilar character.
5. If the adjacent character matches then I am storing the updated location and again running function to get the
    adjacent location.
6. This way checking all the character locations and mapping with their character. If the locations matched with the
    corresponding word then we can print 'true' else 'false'.
'''



#This function is for the first character to get the locations of that character in the 2D array.
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


#This function checks the adjacent character and if it matches according to the word given then it returns location of taht character.
def check(w,k,l,c,d):
    p1,p2=int(k[0]),int(k[1])
    #print('s')
    if p1-1>=0:
        
        if l[p1-1][p2]==w[c] and str(p1-1)+str(p2) not in d:#This condition for checking the element above it.
                #print('1')
                c=c+1
                k=str(p1-1)+str(p2)
                d.append(k)
                #print(c)
                return k
    if p1+1<len(l):
        
        if l[p1+1][p2]==w[c] and str(p1+1)+str(p2) not in d:#This condition for checking the element below it.
                #print('2')
                c+=1
                k=str(p1+1)+str(p2)
                d.append(k)
                #print(c)
                return k
    if p2-1>=0: #This condition for checking the element left to it.
        
        if l[p1][p2-1]==w[c] and str(p1)+str(p2-1) not in d:
                #print('3')
                c+=1
                k=str(p1)+str(p2-1)
                d.append(k)
                #print(c)
                return k
    if p2+1<len(l[0]):
        
        if l[p1][p2+1]==w[c] and str(p1)+str(p2+1) not in d: #This condition for checking the element right to it.
            #print('4')
            c+=1
            k=str(p1)+str(p2+1)
            d.append(k)
            #print(c)
            return k
    return k
    
m1,m2=map(int,input('Enter the row count and column count:').split())#Taking row and column input
b=[]
for i in range(m1):
    b1=[x for x in input().split()]
    b.append(b1)

w=input('Enter the word:')#Taking the input word
n=len(w)
c=1
k=0
i=0
d=[]
l=fun(w,0,b)
for j in range(len(l)):#Iterating in all the locations of the first character of the word.
    k=l[j]
    #d.append(k)
    #lst=list(check(w,k,b,c))
    #d=[]
    #print('hello')
    for q in range(1,len(w)):
        p= check(w,k,b,q,d)  #This function everytime return the adjacent location matched based on the word.
        k=p

print(d)
if len(d)>0 and b[int(d[-1][0])][int(d[-1][1])]==w[-1]: # Finally Checking if the we reached the last element of the word if it matches then 'true' else 'false'
     print('True')
else:
    print('False')
        
                    
                
