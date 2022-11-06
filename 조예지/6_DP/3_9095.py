#[BOJ] 9095 1,2,3 더하기
"""
1 <= n <= 11
[1, 2, 4, 7]
3 = [1, 1, 1], [2, 1], [1, 2], [3]

1) 점화식
DP[n-3]+DP[n-2]+DP[n-1]
"""

DP = [0]*12
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4, 12):
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]


T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N])

