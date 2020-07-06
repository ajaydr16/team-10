for i in range(int(input())):
        n=int(input())
        s=bin(n)[2:]
        s='0'*(8-len(s))+s
        #print(s)
        print(int(s[len(s)//2:]+s[:len(s)//2],2))
        
