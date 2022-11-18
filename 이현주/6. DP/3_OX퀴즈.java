package boj.Nov_11st;

import java.util.Arrays;

/*
[프로그래머스] OX 퀴즈: 2차 시도 성공

1. 1차 시도 실패
- 원인: 연산자를 찾을 때 equals가 아닌 "=="으로 비교하여 정확하게 계산되지 않음

 */
public class OXQuiz {
    public String[] solution(String[] quiz) {

        String[] answer = new String[quiz.length];
        int answerElement = 0;
        int index = 0;
        for (String problem: quiz) {
            String[] splitted = problem.split(" ");
            if (splitted[1].equals("+") ) {
                answerElement = Integer.parseInt(splitted[0]) + Integer.parseInt(splitted[2]);
            } else if (splitted[1].equals("-")){
                answerElement = Integer.parseInt(splitted[0]) - Integer.parseInt(splitted[2]);
            }
            if (answerElement == Integer.parseInt(splitted[4])) {
                answer[index] = "O";
                index ++;
            } else {
                answer[index] = "X";
                index ++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        OXQuiz oxQuiz = new OXQuiz();
        String[] quiz = {"3 - 4 = -3", "5 + 6 = 11"};
        System.out.println(Arrays.toString(oxQuiz.solution(quiz)));
    }
}
