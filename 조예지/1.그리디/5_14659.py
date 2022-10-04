N = int(input())

arr = list(map(int, input().split()))

H = 0
result = 0
cnt = 0
for m in arr:
    #낮은 봉우리는 처치
    if m < H :
        cnt += 1
    #높은 봉우리는 초기화 & 처치한 수 비교해서 더 많으면 저장
    else :
        H = m
        if cnt > result:
            result = cnt
        cnt = 0

#마지막 봉우리까지 비교해주기
if cnt > result:
    result = cnt

print(result)
