package baekjoon;

import java.util.Scanner;

public class BAJ2720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		while (n1 --> 0) {
			int money = sc.nextInt();
			int a= money / 25;
			money %= 25;
			int b = money / 10;
			money%= 10;
			int c = money / 5;
			money %= 5;
			int d = money;

			System.out.println(a + " " + b + " " + c + " " + d);
		
		}

	}
}
