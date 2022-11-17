package boj.Nov_4th;

/*
[BOJ] 1920: 수 찾기
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

import static java.util.Arrays.binarySearch;

public class SearchNum {

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
    public int[] findNum(int[] a, int[] b) {
        int[] answer = new int[b.length]; //0, 1로 채워넣을 예정..
        Arrays.sort(a); //배열 정렬
        //이진탐색
        for (int i = 0; i < b.length; i++) {
            if (binarySearch(a, b[i], 0, a.length-1) == -1) {
                answer[i] = 0; //존재하지 않으면 0 대입
            } else {
                answer[i] = 1; //존재하면 1 대입
            }
        }
        return answer;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        SearchNum searchNum = new SearchNum();

        //대상 배열
        int N1 = Integer.parseInt(br.readLine());
        int[] exArr = new int[N1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N1; i++) {
            exArr[i] = Integer.parseInt(st.nextToken());
        }


        //비교 배열
        int N2 = Integer.parseInt(br.readLine());
        int[] controlArr = new int[N2];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < N2 ; i++) {
            controlArr[i] = Integer.parseInt(st2.nextToken());
        }
        int[] answer = searchNum.findNum(exArr, controlArr);
        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
        br.close();
    }
}
