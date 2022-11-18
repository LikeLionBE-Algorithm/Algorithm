package boj.Nov_17th;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
[BOJ] 1717 집합의 표현
 */
public class ExpressionSet {
    // v= 노드 개수, e= 간선(Union 연산) 개수
    public static int v, e;
    // 노드 개수는 최대 10만 개
    public static int[] parent;

    //특정 원소가 속한 집합 찾기
    public static int findParent(int x) {
        if( x == parent[x]) return x;
        // 루트 노드가 아닐 경우, 루트 노드를 찾을 때까지 재귀 호출
        return parent[x] = findParent(parent[x]);
    }

    // 두 원소가 속한 집합을 합치기
    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        //Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        v = Integer.parseInt(st.nextToken()); // 노드 개수
        e = Integer.parseInt(st.nextToken()); // 연산 개수

        parent = new int[v + 1];

        // 부모를 자기 자신으로 초기화
        for (int i = 1; i <= v ; i++) {
            parent[i] = i;
        }

        // e만큼 연산 입력받기
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (a == 0){
                unionParent(b, c);
            } else if (a == 1) {
                if (findParent(b) == findParent(c)){
                    sb.append("yes" + "\n");
                } else {
                    sb.append("no"+"\n");
                }
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}
