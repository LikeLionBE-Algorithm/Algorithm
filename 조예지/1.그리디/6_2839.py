N = int(input())

M = N//5
result = -1
#5 > 10 > 15 빼면서 3으로 나눠 지는 지 보기
for i in range(M, -1, -1):
    T = N - (5*i)
    if T%3 == 0:
        result = T//3 + i
        break

print(result)