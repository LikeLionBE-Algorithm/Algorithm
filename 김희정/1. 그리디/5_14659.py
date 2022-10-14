'''
BOJ_14659_한조서열정리하고옴ㅋㅋ
[나의 idea]
- 왼쪽부터 자신의 오른쪽 원소와 크기비교 >> 자기보다 작으면 cnt++
- 뒤에 남은 봉우리가 현재 최대값보다 작으면 break >> 더 비교할 필요x
- 이중 for문 사용

[시간복잡도]
- O(n^2)

[실수]
- 문제를 잘못 이해
    : 용이 오른쪽으로 이동하다가 더 높은 봉우리 만나면 멈추는 조건 고려 x
'''

n = int(input())  #봉우리수
heightarr = list(map(int, input().split()))
max_value = 0;

for i in range(n):
    cnt = 0
    #뒤에 남은 봉우리가 현재 최대값보다 작으면, break
    if (n - 1 - i) <= max_value:
        break;
    #자신의 오른쪽 원소들과 크기비교
    for j in range(i+1, n):
        if heightarr[i] > heightarr[j]:
            cnt += 1
        else:
            break
    #최댓값 계산
    if cnt > max_value:
        max_value = cnt
print(max_value)

'''
[other solution]
- 이중 for문 사용 x >> 시간 반으로 줄어듬

[시간 복잡도]
- O(n)

for hill in heightarr:
    if hill > max_value:
        max_value = hill
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
'''


