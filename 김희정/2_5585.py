'''
BOJ_5585_거스름돈
나의 idea : 큰 거부터 계산
'''

money = int(input())
charge = 1000-money
charges = [500,100,50,10,5,1]
count = 0
for i in charges:
    count += charge//i
    charge %= i
print(count)