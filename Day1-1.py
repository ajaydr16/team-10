#Day1-1: COINS - Bytelandian gold coins
dp = {}
dp[0] = 0
dp[1] = 1

def fun(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = max(n, fun(n//2) + fun(n//3) + fun(n//4))
        return dp[n]
i = 10
while(i > 0):
        n = int(input())
        print(fun(n))
        i -= 1