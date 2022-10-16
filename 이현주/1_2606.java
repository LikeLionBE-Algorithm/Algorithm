package net.acmicpc.baekjoon.Oct_15th;
// [BOJ: 2606] 바이러스
// BFS, Graph, Queue

import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Scanner;

// node 객체를 저장할 큐 자료구조 클래스
class Queue<T> {
    class Node<T> {
        private T data;
        private Node<T> next;
        public Node(T data) {
            this.data = data;
        }
    }

    private Node<T> first;
    private Node<T> last;

    //add 메소드
    public void add (T item){
        Node<T> node = new Node<T>(item);

        if (last != null) {
            last.next = node;
        }
        last = node;
        if (first == null) {
            first = last;
        }
    }

    // remove 메소드
    public T remove() {
        if (first == null) {
            throw new NoSuchElementException();
        }

        T data = first.data;
        first = first.next;

        if (first == null) {
            last = null;
        }
        return data;
    }

    // peek 메소드
    public T peek() {
        if (first == null) {
            throw new NoSuchElementException();
        }
        return first.data;
    }

    //isEmpty 메소드
    public boolean isEmpty() {
        return first == null;
    }

}


// 그래프 클래스
class Graph {
    class Node{
        int data;
        LinkedList<Node> adjacent;
        boolean marked;
        Node (int data) {
            this.data = data;
            this.marked = false;
            adjacent = new LinkedList<>();
        }
    }
    Node[] nodes;
    Graph(int size) {
        nodes = new Node[size];
        for (int i = 0; i < size; i++) {
            nodes[i] = new Node(i) ; //nodes 배열에 Node 객체를 저장한다.
        }
    }

    void addEdge(int i1, int i2){ // 노드 배열의 i1번째 노드, i2번째 노드의 관계를 저장하는 함수
        Node n1 = nodes[i1]; //nodes 배열의 i1 인덱스에 들어있는 Node 객체를 Node n1 변수에 담는다.
        Node n2 = nodes[i2]; //nodes 배열의 i2 인덱스에 들어있는 Node 객체를 Node n2 변수에 담는다.
        if (!n1.adjacent.contains(n2)){
            n1.adjacent.add(n2);
        }
        if (!n2.adjacent.contains(n1)) {
            n2.adjacent.add(n1);
        }
    }


    // 인자가 주어지지 않을 경우 0번째 노드부터 너비우선탐색을 시작한다.
    void bfs() {
        bfs(0);
    }

    // 인자값으로 주어진 인덱스 노드부터 너비우선탐색을 시작한다.
    void bfs(int index) {
        Node root = nodes[index];
        int count = 0;
        Queue<Node> queue = new Queue<Node>();
        queue.add(root);
        root.marked = true;
        while(!queue.isEmpty()) {
            Node r = queue.remove();
            for (Node n : r.adjacent) {
                if (n.marked == false) {
                    n.marked = true;
                    queue.add(n);
                }
            }
            count ++;
        }
        System.out.println(count-1);
    }

    // 노드에 방문하면 노드의 data를 출력해주는 visit 메소드
    void visit(Node n) {
        System.out.print(n.data + " ");
    }
}

public class Virus {
    public static void main(String[] args) {
        // 컴퓨터의 수 받기 (1~100)
        Scanner sc = new Scanner(System.in);
        int computerNum = sc.nextInt();
        Graph g = new Graph(computerNum+1);

        // 간선 수 받기
        int directLink = sc.nextInt();

        // directLink만큼 간선 연결 관계 입력
        for (int i=0; i < directLink; i++) {
            int i1 = sc.nextInt();
            int i2 = sc.nextInt();
            g.addEdge(i1, i2);
        }
        g.bfs(1);
    }
}