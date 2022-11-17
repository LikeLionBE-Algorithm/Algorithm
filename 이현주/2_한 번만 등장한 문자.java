package boj.Nov_16th;

import java.util.*;

/*
[프로그래머스] 한 번만 등장한 문자
https://school.programmers.co.kr/learn/courses/30/lessons/120896
자료구조- Map or Set

1. 매개변수 String s를 순회하며 key는 각각의 글자를, value는 글자의 갯수를 올려준다.
2. value가 1인 key들만 사전 순으로 정렬한 스트링을 리턴한다.

-> 실행시간이 정말 오래 걸린다.
 */
public class CharAppearedOneTime {
    public String solution(String s) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();
        List<String> list = new ArrayList<>();
        String[] splitted = new String[s.length()];
        splitted = s.split("");

        for (int i = 0; i < splitted.length; i++) {
            if (map.containsKey(splitted[i])) {
                map.put(splitted[i], map.get(splitted[i]) + 1);
            } else {
                map.put(splitted[i], 1);
            }
        }

        Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
        for (Map.Entry<String, Integer> entry : entrySet) {
            if (entry.getValue().equals(1)) {
                list.add(entry.getKey());
            }
        }

        Collections.sort(list);
        for (String c :list) {
            answer = answer + c;
        }

        return answer;
    }
}
