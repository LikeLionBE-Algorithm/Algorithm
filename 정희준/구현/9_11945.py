import sys 
n,m = map(int,sys.stdin.readline().split())
result = []
for i in range(n):
    x = []
    a = sys.stdin.readline().strip()
    for l in a:
        x.insert(0,l)
    result.append("".join(x))
for k in result:
    print(k)