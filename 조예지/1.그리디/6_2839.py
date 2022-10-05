N = int(input())

M = N//5
result = -1
for i in range(M, -1, -1):
    T = N - (5*i)
    if T%3 == 0:
        result = T//3 + i
        break

print(result)