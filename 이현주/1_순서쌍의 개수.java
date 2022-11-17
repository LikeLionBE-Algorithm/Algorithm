package boj.Nov_16th;

/*
[프로그래머스] 순서쌍의 개수 - 통과
https://school.programmers.co.kr/learn/courses/30/lessons/120836
ㅇ idea
  - 매개변수 n을 1부터 n까지의 수로 나눈다. -> for문
  - 나누었을 때 나머지가 0이 될 때, 카운트를 1 올려준다.
  - 최종 카운트 수 리턴
 */

public class OrderedPair {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0)
                answer+=1;
        }
        return answer ;
    }
}