def solution(answers):
    x1 = [1,2,3,4,5]
    x2 = [2,1,2,3,2,4,2,5]
    x3 = [3,3,1,1,2,2,4,4,5,5]
    total = [x1*((len(answers)//5)+1),x2*((len(answers)//8)+1),x3*((len(answers)//10)+1)]
    result = []
    for i in range(3):
        count = 0 
        for l in range(len(answers)):
            if answers[l] == total[i][l]:
                count+=1
        result.append(count)
    answers.clear()
    for i in range(3):
        if result[i] == max(result):
            answers.append(i+1)
    return answers


