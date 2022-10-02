T = int(input())
coins = [25, 10, 5, 1]
for _ in range (T):
  chg = int(input())
  for c in coins :
    n = chg // c
    chg %= c
    print(n, end=" ")