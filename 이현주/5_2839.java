package net.acmicpc.baekjoon.Oct_6th;

//2839번: 설탕 배달

import java.util.Scanner;

public class SugarDelivery_2839 {
    public static void main(String[] args) {
        int SugarBag5Kg = 0;
        int SugarBag3Kg = 0;
        int RemainderSugar = 0;

        Scanner sc = new Scanner(System.in);

        int SugarOrder = sc.nextInt(); // 배달해야하는 설탕의 무게 N kg 입력

        if ((SugarOrder % 5)%3 != 0){
            System.out.println(-1);
        }else {
            SugarBag5Kg = SugarOrder/5;
            RemainderSugar = SugarOrder%5;

            if ((SugarOrder%3==0)){
                SugarBag3Kg = RemainderSugar/3;
            }

            int SugarBagNum = SugarBag5Kg + SugarBag3Kg;

            System.out.println(SugarBagNum);
        }



        // (N % 5) % 3 계산 결과 값이 존재한다면 '-1' 출력
            // sugarBag5Kg = N을 5로 나눈 몫만 넣기
            // sugarBag3Kg = "N을 5로 나눈 나머지"에 대해 이 수가 3의 배수여야 한다.
            // 이 조건 충족 시, 3으로 나눈 몫을 넣기.
            // sugarBag5Kg + sugarBag3Kg 리턴 .

        // answer = 설탕 봉지 수를 출력
            // (N / 5) + ((N % 5) / 3)


    }

}
