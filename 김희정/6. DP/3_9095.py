'''
[BOJ] 9095 1,2,3 더하기
나의 idea :
'''

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + 1
    print(dp[n])