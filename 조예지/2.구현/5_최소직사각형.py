def solution(sizes):
    M1 = 0
    M2 = 0
    for i in range(len(sizes)):
        size = sorted(sizes[i])
        M1 = max(size[0], M1)
        M2 = max(size[1], M2)
    answer = M1*M2
    return answer

# sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes2 =[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# sizes3 =[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
#
# print(solution(sizes1))
# print(solution(sizes2))
# print(solution(sizes3))
