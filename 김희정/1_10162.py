'''
BOJ_10162_전자레인지
A : 5분 = 300초, B = 1분 = 60초, C = 10초
나의 idea : 큰 거부터 나눈다.
T = T - 300*numA >> T %= 300
'''
#
#
# T = T - 300*numA >> T %= 300
T = int(input())
buttons = [300,60,10]
if T%10 != 0:
    print(-1)
else:
    for i in buttons:
        print(T//i, end=' ')
        T %= i