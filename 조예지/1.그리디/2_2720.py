T = int(input())

for _ in range (T):
  chg = int(input())

  Q = chg // 25
  chg %= 25
  D = chg // 10
  chg %= 10
  N = chg // 5
  P = chg % 5
  print (Q, D, N, P)