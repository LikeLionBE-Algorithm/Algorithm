package boj.Nov_11st;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
[프로그래머스] 모음 제거: 실패,,
1차 시도- 반복문 스코프가 잘못되어 잘못된 답이 나온다.
2차 시도- 아무래도 뭐가 틀렸는지 모르겠다....
3차 시도- relace 함수 사용하여 성공. -> 실패,,

답안 참고...

[idea]
1. 문자열을 순회하면서 vowel의 다섯 원소와 비교한다.
2. 일치할 경우 삭제한다.
(조건) 순서가 틀어지거나 문자열에 있던 공백을 삭제하면 안된다.
 */
public class DeleteVowel {

    // 나의 풀이 (실패)
    /*
    public String solution(String my_string) { //"bus"
        String[] vowels = new String[] {"a", "e", "i", "o", "u"};
        String[] my_strings = my_string.split(""); //nice to meet you
        String answer = "";

        for (int i = 0; i < my_strings.length; i++) {
            for (String vowel: vowels) {
                String c = String.valueOf(my_string.charAt(i));
                if (c.contains(vowel)) {
                    deletedStr = my_string.replace(c, "");
                }
            }
        }
        return answer;
    }
     */

    public String solution(String my_string) {
        // ArrayList 초기화
        List<String> vowels = Arrays.asList("a", "e", "i", "o", "u");

        String answer = "";
        for (int i = 0; i < my_string.length(); i++) {
            if (!vowels.contains(String.valueOf(my_string.charAt(i)))) {
                answer = answer + my_string.charAt(i);
            }
        }
        return answer;
    }


    public static void main(String[] args) {
        DeleteVowel dv = new DeleteVowel();
        String my_string = "nice to meet you";
        System.out.println(dv.solution(my_string));

    }
}
