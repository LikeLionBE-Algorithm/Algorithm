package net.acmicpc.baekjoon.Oct_6th;
// 14659: 한조서열정리하고옴ㅋㅋ

import java.util.Arrays;
import java.util.Scanner;

public class HanjoClass_14659 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int PeakNum = sc.nextInt(); //입력받은 봉우리 수

        int[] PeakHeightArr = new int[PeakNum]; //봉우리별 높이를 저장하는 배열

        for (int i = 0; i <PeakHeightArr.length; i++ ){
            PeakHeightArr[i] = sc.nextInt();
        }

        System.out.println(Arrays.toString(PeakHeightArr));

        int[] KillEnemyNumArr = new int[PeakNum]; //처치한 적의 수

        int BiggestKillEnemyNum = 0; //봉우리에서 가장 많은 적을 처치한 수

        int KillEnemyNum = 0; //변수 선언

        // 1: PeakHeightArr의 값 비교
        for (int i = 0; i<PeakHeightArr.length; i++){
            for (int j = i+1; j<PeakHeightArr.length; j++){
                if (PeakHeightArr[i] > PeakHeightArr[j]){
                    KillEnemyNum ++;
                    System.out.println("비교한 봉우리 번호는" + i +"와"+ j + "이고, 죽인 수는" + KillEnemyNumArr[i]);
                    System.out.println("------------------");
                }
                else {
                    KillEnemyNumArr[i] = KillEnemyNum;
                    System.out.println("봉우리 번호는 "+ j + "이고, 죽인 수는" + KillEnemyNumArr[i]);
                    System.out.println("------------------");
                    break;
                }

            }
        }

        // 2: KillEnemyNumArr의 가장 큰 수를 반환
        for (int i = 0; i < KillEnemyNumArr.length; i++){
            if (BiggestKillEnemyNum < KillEnemyNumArr[i]) {
                BiggestKillEnemyNum = KillEnemyNumArr[i];
            }

        }

        System.out.println("가장 많은 적을 해치운 수는 " + BiggestKillEnemyNum);
    }
}
