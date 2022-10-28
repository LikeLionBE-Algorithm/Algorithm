'''
[BOJ] 10989 수 정렬하기 3
나의 idea
1. 배열에 담고 sort()함수로 정렬 후 print >> 메모리 초과(10,000,000개를 저장하려 해서)
2. 계수 정렬 이용(Count Sort) : 10,000 + 1 크기의 리스트만으로도 가능
'''
import sys

n = int(sys.stdin.readline()) #수의 개수
count = [0]*10001
for _ in range(n):
    temp = int(sys.stdin.readline())
    count[temp] += 1
for i in range(len(count)):
    for _ in range(count[i]):
        print(i)



