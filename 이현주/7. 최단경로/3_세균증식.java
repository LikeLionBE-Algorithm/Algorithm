package boj.Nov_16th;

/*
세균의 수 = n마리 x 2^t (t= time, n=세균의 수)
https://school.programmers.co.kr/learn/courses/30/lessons/120910
 */
public class BacterialGrowth {
    public int solution(int n, int t) {
        int answer = 0;
        int time = 1;
        for (int i = 0; i < t; i++) {
            time = time * 2;
        }
        answer = n * time;
        return answer;
    }
}
