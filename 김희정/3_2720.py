'''
BOJ_2720_세탁소 사장 동혁
나의 idea : 큰 거부터 계산 :  //, %이용
'''

coins = [25,10,5,1]
n = int(input())
for _ in range(n):
    charge = int(input())
    for i in coins:
        print(charge//i,end=" ")
        charge %= i