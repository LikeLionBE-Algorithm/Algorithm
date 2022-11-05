#[BOJ] 1463 1로 만들기
"""
함수
결과는 1
연산을 사용하는 횟수의 최소값
통과x
"""

num = int(input())

cnt = [0]*(num+3)
cnt[1] = 0
cnt[2] = 1
cnt[3] = 1


for N in range(4, num+1):
    if N%3 == 0:
        if N%2 == 0:
            cnt[N] = min(cnt[N//2]+1, cnt[N//3]+1, cnt[N-1]+1)
        else:
            cnt[N] = min(cnt[N//3]+1, cnt[N-1]+1)
    elif N%2 == 0:
        cnt[N] = min(cnt[N//2]+1, cnt[N-1]+1)
    else:
        cnt[N] = cnt[N-1]+1
print(cnt[num])