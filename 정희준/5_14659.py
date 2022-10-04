n = int(input())
x = list(map(int,input().split()))
y = []
m = x[0]
count = 0 
for i in x[1:]:
    if m > i :
        count +=1
    elif m <=i:
        y.append(count)
        count = 0 
        m = i 
y.append(count)
print(max(y))