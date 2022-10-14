'''
BOJ_2839_설탕 배달
나의 idea :
'''
n = int(input())
temp = n
cnt = 0
result = 0

while temp > 0:
    temp -= 5
    cnt += 1
    if temp%3 == 0:
        cnt += temp//3
        temp %= 3
        break
if temp == 0:
    result = cnt
else:
    temp = n
    cnt = 0
    while temp > 0:
        temp -= 3
        cnt += 1
        if temp % 5 == 0:
            cnt += temp // 5
            temp %= 5
            break
    if temp!=0:
        result = -1
    else:
        result = cnt
print(result)



