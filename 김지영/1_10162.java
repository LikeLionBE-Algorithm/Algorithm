package baekjoon;

import java.util.Scanner;

public class BAJ10162 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] arr = {300,60,10};
		String result="";
		
		while(true) {
		if(num % 10 != 0) {
			System.out.println(-1);
			break;
		}
		for(int i=0; i<arr.length; i++) {
			result += num/arr[i]+ " ";
			num %= arr[i];

		}
		System.out.println(result);
		break;
		}
	}
}