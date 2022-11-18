package net.acmicpc.baekjoon;

import java.util.Scanner;

public class Main_5585 {
    public static void main(String[] args) {
        int price; //물건 가격
        int changePrice; //잔돈
        int changeCount; // 잔돈 총 매수
        String error = "error";
        Scanner sc = new Scanner(System.in);
        price = sc.nextInt();
        changePrice = 1000 - price;
        if (price > 1000) {
            System.out.println(error);
        }
        int count_500 = changePrice / 500;
        changePrice = changePrice % 500;

        int count_100 = changePrice / 100;
        changePrice = changePrice % 100;

        int count_50 = changePrice / 50;
        changePrice = changePrice % 50;

        int count_10 = changePrice / 10;
        changePrice = changePrice % 10;

        int count_5 = changePrice / 5;
        changePrice = changePrice % 5;

        int count_1 = changePrice / 1;

        changeCount = count_500 + count_100 + count_50 + count_10 + count_5 + count_1;
        System.out.println(changeCount);




    }

}
