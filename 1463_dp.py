import sys

sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
dp = [0] * (n+1)
# print(dp)
x = n
for i in range(2, n+1) :
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])