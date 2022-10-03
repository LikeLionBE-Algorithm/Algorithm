package net.acmicpc.baekjoon;

import java.util.Scanner;

class availableDayCalc {
    private int L, P, V;
    private int availableDay;

    availableDayCalc(int L, int P, int V) {
        this.L = L;
        this.P = P;
        this.V = V;
    }

    void setAvailableDay(int L, int P, int V){
        this.L = L;
        this.P = P;
        this.V = V;
    }

    void Calc() {
        availableDay = (( V / P ) * L ) + ( V % P );
        this.availableDay = availableDay;
    }

    int print() {
        return availableDay;
    }
}

public class camping_4796 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        while (true) {
            int L = sc.nextInt();
            int P = sc.nextInt();
            int V = sc.nextInt();
            availableDayCalc A = new availableDayCalc(L, P, V);
            if ( L == 0 && P == 0 && V == 0) {
                A.Calc();
                A.print();
                break;
            }
        }


    }

}