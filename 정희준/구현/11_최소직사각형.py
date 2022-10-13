def solution(sizes):
    total1 = []
    total2 = []
    for i in sizes:
        total1.extend(i)
    for l in sizes:
        l.pop(l.index(max(l)))
    for k in sizes:
              total2.extend(k)
             
    return max(total1) * max(total2)