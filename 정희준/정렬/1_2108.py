from collections import Counter # collections 모듈의 counter 클래스 사용 불러오기 
import sys
n = int(sys.stdin.readline()) # 수의 개수 
x = [] # 입력되는 정수들을 저장할 리스트 
for i in range(n):
    a = int(sys.stdin.readline())
    x.append(a)
x.sort()
if ((sum(x)/n) - (sum(x)//n)) >= 0.5: # 0.5가 넘으면 반올림 
    print((sum(x)//n)+1)
else:
    print(sum(x)//n) 

print(x[n//2]) # 오름차순 후 중앙 값 

count = Counter(x).most_common() # counter 클래스에서 제공하는 데이터 개수가 많은 순으로 정렬되어 리턴하는 most_common() 메서드 사용 
if len(count) > 1 and count[0][1] == count[1][1]: # 내림차순 정렬되고 0,1 번째 값이 같다면 
    print(count[1][0]) # 이미 위에서 오름차순 정렬을 하였기 때문에 두번째로 작은 값인 1번째 자리 출력 
else:
    print(count[0][0]) # 아니라면 가장 큰 값인 0번째 자리 출력 
"""
y = list(set(x))
x_max = 1
for l in y:
    if x_max == x.count(l):
        result.append(l)
    elif x_max < x.count(l):
        result = []
        result.append(l)
        x_max = x.count(l)
if len(result) > 1:
    print(result[1])
else:
    print(result[0])
"""

print(x[-1] - x[0]) # 오름차순으로 정렬된 x 리스트의 가장 큰 값인 끝 인덱스 값과 가장 작은 값이 0번째 인덱스 값의 차를 출력 