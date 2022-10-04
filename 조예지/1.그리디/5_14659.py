N = int(input())

arr = list(map(int, input().split()))
result = 0

for i in range(len(arr)-1) :
    cnt = 0
    for j in range(i+1, len(arr)) :
        if arr[i]>arr[j]:
            cnt += 1
        else:
            break
    if cnt > result :
        result = cnt
        # 뒤에 볼 필요가 없으면 탈출
        if (i+result*2) >= len(arr) :
            break

print(result)