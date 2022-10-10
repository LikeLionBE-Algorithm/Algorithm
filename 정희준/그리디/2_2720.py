import math
a = int(input())
n = 1
m = 1
x = [25,10,5,1]
y = []
z = []
while n <=a:
    b = int(input())
    y.append((b))
    n +=1
for i in y:
    for j in x:
        total  = (i//j)
        i = i - (total*j)
        z.append(total)
c=0
d=1
e=2
f=3
while m <=a:
    print(int(z[c]),int(z[d]),int(z[e]),int(z[f]))
    c+=4
    d+=4
    e+=4
    f+=4
    m+=1
