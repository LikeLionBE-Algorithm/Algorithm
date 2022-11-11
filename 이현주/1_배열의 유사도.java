package boj.Nov_11st;
/*
[프로그래머스] 배열의 유사도

1차 시도: 실패
궁금한 점: 인텔리제이에서는 '==' 조건이 먹혔는데 왜 프로그래머스에서는 안될까..
2차 시도: 성공 (equals로 변경 완료)
 */

public class SimilarArr {

    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for (String s1_Str: s1) {
            for (String s2_Str: s2) {
                if (s1_Str.equals(s2_Str)) {
                    answer = answer + 1;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        SimilarArr sa = new SimilarArr();
        String[] s1 = {"a", "b", "c"};
        String[] s2 = {"com", "b", "d", "p", "c"};
        String[] s3 = {"n", "omg"};
        String[] s4 = {"m", "dot"};

        System.out.println(sa.solution(s1, s2));
        System.out.println(sa.solution(s3, s4));
    }
}
