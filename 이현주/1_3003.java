package net.acmicpc.baekjoon.Oct_11th;

import java.util.Arrays;
import java.util.Scanner;

public class chess {
    public static void main(String[] args) {
        final int[] pieceNum = {1, 1, 2, 2, 2, 8};
        int[] inputArr = new int[6];
        int[] answerArr = new int[6];

        Scanner sc = new Scanner(System.in);

        // 흰색 피스 개수 입력 0~10
        for (int i = 0; i <inputArr.length; i++ ){
            inputArr[i] = sc.nextInt();
        }

        for (int i = 0; i < answerArr.length; i++) {
            answerArr[i] = pieceNum[i] - inputArr[i];
        }

        for (int i = 0; i < answerArr.length; i++){
            System.out.print(answerArr[i]+" ");
        }

    }
}
