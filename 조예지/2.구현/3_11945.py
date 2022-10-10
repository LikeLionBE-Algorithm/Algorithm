N, M = map(int, input().split())
for _ in range(N):
    #arr=input()
    arr = list(input())
    #print(a[::-1])
    for i in range(M-1, -1, -1):
        print(arr[i], end='')
    print()

