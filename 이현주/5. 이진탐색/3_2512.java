package boj.Nov_4th;

import java.util.Arrays;
import java.util.Scanner;
/*
[BOJ] 2512: 예산
 */
public class Budget {
    private static int[] arr;
    private static long answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 지자체 수
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr); //110 120 140 150
        long M = sc.nextLong(); //총 예산

        long left = 0; // 110
        long right = arr[N-1]; // 150

        while (left <= right) {
            long mid = (left + right) / 2; //상한선
            long sum = 0; // 요청 예산액 총합
            for (int money : arr) {
                if (money >= mid) { //요청 예산액 초과시
                    sum += mid; //중간값만 더해준다.
                }
                else {
                    sum += money; //요청 예산액 미초과시, 해당 값을 그대로 더해준다.
                }
            }
            if (sum > M) { // 예산 초과일 경우
                right = mid - 1; // 상한선을 줄여본다.
            } else { // 요청 예산액과 지급가능한 예산액이 같거나, 요청예산액이 더 적을 경우
                left = mid + 1; // 상한선을 늘린다.
                answer = Math.max(answer, mid); // 최대값을 준다.
            }
        }
        System.out.println(answer);
    }
}
