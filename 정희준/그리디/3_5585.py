n = int(input())
count = 0 
x = 1000-n
while True:
    if x>=500:
        count+=(x//500)
        x %=500
    elif x>= 100:
        count+=(x//100)
        x %= 100
    elif x>= 50:
        count+=(x//50)
        x %=50
    elif x>= 10 :
        count+=(x//10)
        x %=10
    elif x>=5:
        count+=(x//5)
        x %=5
    elif x>=1:
        count+=(x//1)
        x %=1
    if x == 0:
        break
print(count)
