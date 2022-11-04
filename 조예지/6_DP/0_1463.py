#[BOJ] 1463 1로 만들기
"""
함수
결과는 1
연산을 사용하는 횟수의 최소값
"""

num = int(input())

cnt = [0]*(num+1)
cnt[1] = 0
cnt[2] = 1
cnt[3] = 1


for N in range(4, num+1):
    if N%3 == 0:
        cnt[N] = cnt[N//3]+1
    elif N%3 == 1:
        cnt[N] = cnt[N-1]+1
    else:
        if N%2 == 0:
            cnt[N] = cnt[N//2]+1
        else:
            cnt[N] = cnt[N-1]+2

print(cnt[num])