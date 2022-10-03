package baekjoon;

import java.util.Scanner;

public class BAJ5585 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = 1000-sc.nextInt();
		int money =0;
		int[] arr = {500,100,50,10,5,1};
		for(int i =0; i<arr.length; i++) {
			if(num%arr[i] >=0) {
				money += num/arr[i];
				num %= arr[i];
			}
		}
		System.out.println(money);
	}
}
