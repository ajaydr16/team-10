for _ in range(int(input())):
    n=int(input())
    print(len([(i^j) for i in range(1,n) for j in range(i+1,n+1) if (i^j <= n)]))

                
