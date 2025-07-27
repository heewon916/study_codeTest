package d3;

import java.io.*; 
import java.util.*; 
public class Solution_10844 {
	static boolean isStairsNum(int N) {
		String strN = Integer.toString(N);
		int[] mat = new int[strN.length()]; 
		
		for(int i=0;i<strN.length(); i++) {
			mat[i] = strN.charAt(i)- '0'; 
		}
	}

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();		
		int N = Integer.parseInt(br.readLine());
		
		if(N == 1) System.out.println(9);
		else {
			
		}
		int res = 0; 
		for(int i=1; i<=N; i++) {
			
		}
		
		
		
	}

}
