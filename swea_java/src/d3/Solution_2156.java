package d3;


import java.io.*; 
import java.util.*; 

public class Solution_2156 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st; 
		
		int N = Integer.parseInt(br.readLine());
		int[] mat = new int[N]; 
		for(int i=0; i<N; i++) {
			mat[i] = Integer.parseInt(br.readLine());
		}
		
		int[] dp = new int[N];
		int res = 0; 
		if(N<=2) {
			for(int i=0; i<N; i++) {
				res += mat[i]; 
			}
			System.out.println(res);
		}else {
			dp[0] = mat[0]; dp[1] = mat[0] + mat[1];
			dp[2] = Math.max(Math.max(dp[1], mat[0]+mat[2]), mat[1]+mat[2]);
			for(int i=3; i<N; i++) {
				dp[i] = Math.max(Math.max(dp[i-1], mat[i]+dp[i-2]), mat[i]+mat[i-1]+dp[i-3]);
			}
			System.out.println(dp[N-1]);
		}
		
	}
}
//6
//6
//10
//13
//9
//8
//1
