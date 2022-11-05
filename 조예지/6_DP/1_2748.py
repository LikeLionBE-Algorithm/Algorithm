#[BOJ] 2748 피보나치 수2
num = int(input())

fibo = [0] * 90
fibo[0] = 0
fibo[1] = 1

for i in range(2, num+1):
    fibo[i] = fibo[i-2] + fibo[i-1]
print(fibo[num])