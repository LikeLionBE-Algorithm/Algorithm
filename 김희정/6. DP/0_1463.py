'''
[BOJ] 1463 1로 만들기
나의 idea : 시간복잡도를 줄이기 위해 DP 사용
점화식 : dp[i] = dp[i-1 or i//3 or i//2] + 1

dp[2] = 2//2 = 연산횟수 1
dp[3] = 3//3 = 연산횟수 1
dp[4] = 4//2 , 2//2 = 연산횟수 2
        1 + dp[2]
dp[10] = 10-1, 9//3, 3//3 = 연산 횟수 3
         1 + dp[9]
'''
import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)  # 연산 횟수 저장
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
