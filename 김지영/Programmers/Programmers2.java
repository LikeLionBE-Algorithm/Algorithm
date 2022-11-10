package javaPrac;

public class Programmers2 {
	    public String[] solution(String[] quiz) {
	        String[] answer = new String[quiz.length];
	        for(int i = 0 ; i < quiz.length;i++){
	            String[] str = quiz[i].split(" ");
	            int a = Integer.parseInt(str[0]);
	            int b = Integer.parseInt(str[2]);
	            int c = Integer.parseInt(str[4]);
	            if(str[1].equals("-")){
	                if(c == a-b){
	                    answer[i] = "O";
	                }else{
	                    answer[i] = "X";
	                }
	            }else if(str[1].equals("+")){
	                if(c == a+b){
	                    answer[i] = "O";
	                }else{
	                    answer[i] = "X";
	                }
	            }
	        }
	        return answer;
	    }
	}