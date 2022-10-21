import sys 
n = int(sys.stdin.readline())
result = []
for i in range(n):
    remember = []
    x = sys.stdin.readline().strip()
    remember = [x[0]]
    for l in x[1:]:
        if remember == []:
            remember.append(l)
        elif "(" == remember[-1] and l == ")":
            remember.pop()
        else:
            remember.append(l)
    if remember == []:
        result.append("YES")
    else:
        result.append("NO")

for k in result:
    print(k) 

