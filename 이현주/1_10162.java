package net.acmicpc.baekjoon;

import java.util.Scanner;

class microwave {
    private int time;
    private int ClickButtonA, ClickButtonB, ClickButtonC;
    private int impossible = -1;

    public microwave(int T){
        this.time = T;
    }

    public int getClickButtonA() {
        if (time / 300 == 0) {
            ClickButtonA = 0;

        } else {
            ClickButtonA = time / 300;
            this.time = time % 300;
        }
        return this.ClickButtonA = ClickButtonA;
    }

    public int getClickButtonB() {
        if ((time % 300 == 0) && (time / 60 ==0)) {
            ClickButtonB = 0;
        }else {
            ClickButtonB = time / 60 ;
            this.time = time % 60;
        }
        return this.ClickButtonB= ClickButtonB;
    }

    public int getClickButtonC() {
        if ((time % 300 == 0) && (time % 60) == 0 && (time / 10) ==0 ){
            ClickButtonC = 0;
        }else if((time % 10 > 0)){
            System.out.println(impossible);
        }else {
            ClickButtonC = time / 10;
        }
        return this.ClickButtonC = ClickButtonC;
    }

    public void getTimes(){
        System.out.println(ClickButtonA +" "+ ClickButtonB + " " + ClickButtonC);
    }

}
public class microWave_10162 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("냉동음식의 조리 시간을 입력하세요: ");
        int time = sc.nextInt(); //정수로 입력받은 조리 시간을 time에 저장한다.
        microwave Microwave = new microwave(time);
        Microwave.getClickButtonA();
        Microwave.getClickButtonB();
        Microwave.getClickButtonC();
        Microwave.getTimes();
    }

}