package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ1920 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] A = new int[N]; // 배열길이
		for(int i = 0; i < N; i++) { // 배열 길이 만큼 for문 돌려 배열값넣기
			A[i]  = sc.nextInt();
		}
		Arrays.sort(A); // 정렬
		int M = sc.nextInt();
		for(int i = 0; i<M; i++) {  // M의 개수만큼 반복
			boolean find = false; 
			int target = sc.nextInt(); //찾아야하는 수
			//이진탐색
			int start =0; // 시작인덱스
			int end = A.length-1; // 종료인덱스
			while(start <= end) {
				int midi = (start + end)/2; //중간인덱스
				int midV = A[midi];
				if(midV > target) {  //중앙값>target
					end = midi -1; // 종료인덱스 = 중간인덱스 -1
				}else if (midV < target) { //중앙값 < target
					start = midi + 1; //시작인덱스 = 중간 인덱스 +1
				}else {
					find = true; //찾았으므로 반복문 종료하기
					break;
				}
			}
			if(find) {
				System.out.println(1); //찾았음
			}else {
				System.out.println(0);
			}
		}
	}
}
