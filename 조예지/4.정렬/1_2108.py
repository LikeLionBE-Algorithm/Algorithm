#2108 통계학
"""
시~간~초~과~

Counter 모듈
- dictionary를 확장하고 있어서 사전에서 제공하는 API 사용가능
- 중복된 데이터가 저장된 배열을 인자로 넘기면 몇 번 나오는 지 딕셔너리 형태로 반환한다.
- most_common() : 데이터 개수가 많은 순으로 정렬된 배열을 반환
    - 인자로 정수를 넘기면 K개의 데이터만 반환
"""
import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

#산술평균
avg = round(sum(arr)/len(arr))
print(avg)

#중앙값
arr.sort()
idx = int((len(arr)-1)/2)
print(arr[idx])

#최빈값
frequency = Counter(arr).most_common(2)
if len(frequency) > 1:
    if frequency[1][1] == frequency[0][1]:
        print(frequency[1][0])
    else:
        print(frequency[0][0])
else:
    print(frequency[0][0])


#범위
print(arr[-1]-arr[0])


"""
시간초과 코드
frequent = []
max = 0
for i in setarr:
    cnt = arr.count(i)
    if cnt >= max:
        max = cnt
        frequent.append(i)
if len(frequent) > 1:
    print(sorted(frequent)[1])
else:
    print(frequent[0])
"""
'''
#f-string
print(f'f-string example4 : {num1:.3f}')

#반올림
>>> round(3.1415, 2)   #결과는 3.14
'''
