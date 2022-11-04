package boj.Nov_4th;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
(풀이 실패) hashmap 사용해서 다시 풀어보기
[BOJ] 10816: 숫자 카드 2
 */
public class NumCard2 {

    private static int binarySearch(int[] arr, int target, int start, int end){
        while (start <= end) {
            int mid = (start+end)/2;
            if(arr[mid] == target) {
                return mid;
            } else if (arr[mid] > target) { //찾고자 하는 값보다 중간값이 크다..
                end = mid - 1;
            } else { //찾고자 하는 값이 중간값보다 크다..
                start = mid + 1;
            }
        }
        return -1;
    }

    public int[] countNum(int[] myCard, int[] CardSet) {
        int[] answer = new int[CardSet.length];
        Arrays.fill(answer, 0);
        Arrays.sort(myCard);

        //이진탐색
        for (int i = 0; i < myCard.length; i++) {
            int targetIdx = binarySearch(CardSet, myCard[i], 0, CardSet.length - 1);

            if (targetIdx == -1) {
                answer[i] = 0; //존재하지 않으면 0 대입
            } else () {

            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        NumCard2 numCard2 = new NumCard2();

        //대상 배열
        int N1 = Integer.parseInt(br.readLine());
        int[] Card1 = new int[N1]; //상근이의 카드
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N1; i++) {
            Card1[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(Arrays.toString(Card1));

        //비교 배열
        int N2 = Integer.parseInt(br.readLine());
        int[] Card2 = new int[N2]; //비교할 카드모음
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < N2 ; i++) {
            Card2[i] = Integer.parseInt(st2.nextToken());
        }
        System.out.println(Arrays.toString(Card2));

        int[] answer = numCard2.countNum(Card1, Card2);
        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }
}
