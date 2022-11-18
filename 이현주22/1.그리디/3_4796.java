package net.acmicpc.baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.text.ParseException;
import java.util.StringTokenizer;

public class camping_4796 {
    public static void main(String[] args) throws IOException, ParseException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int L = 0; //캠핑장 최대 사용 가능 일수
        int P = 0; //연속 일수
        int V = 0; //휴가 일수
        int i = 0; //케이스 번호

        while (true) {
            int total;
            i ++; //케이스 번호 증가

            st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());

            if (V == 0) {
                break;
            }
            if (V%P > L) {
                total = (V / P) * L + L;
            }else {
                total = (V / P) * L + (V % P);
            }

            bw.write("Case "+ i + ":" + total + "\n");
        }

        bw.close();
        br.close();


    }

}
