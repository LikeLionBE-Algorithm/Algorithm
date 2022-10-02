P = int(input())

chgs = [500, 100, 50, 10, 5, 1]

total = 1000 - P
sum = 0
for c in chgs:
  n = total // c
  total %= c
  sum += n
print(sum)