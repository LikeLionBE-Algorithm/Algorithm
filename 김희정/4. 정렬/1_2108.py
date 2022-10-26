'''
[BOJ] 2108 통계학
나의 idea : 최빈값 - dict으로 구현
- 리스트를 딕셔너리 key로 : dictionary = dict.fromkeys(string_list,0)
'''

n = int(input()) #수의 갯수
arr = []
for _ in range(n):
    arr.append(int(input()))
#1. 산술평균
average = round(sum(arr) / n)
print(average)

#2. 중앙값
arr.sort()
center = arr[n//2]
print(center)

#3. 최빈값 - dict
count = dict()
for elem in arr: #기본 셋팅
    count[elem] = 0
for elem in arr:
    count[elem] += 1
#최빈값 여러개일때 두 번째로 작은 값 출력
maxf_value = max(count.values())
max = set()
for k,v in count.items():
    if v == maxf_value:
        max.add(k)
sortedlist = list(max)
sortedlist.sort()
if len(sortedlist) > 1:
    print(sortedlist[1])
else:
    print(sortedlist[0])

#4. 범위
max_value = arr[len(arr)-1]
min_value = arr[0]
print(max_value-min_value)
