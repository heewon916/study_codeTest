package d3;

import java.io.*;
import java.util.*; 

public class Solution_5215 {
	static int max_score = 0; 
	public static void backtracking(int start, int sum_score, int sum_cal, int[][] combo, int N, int limit) {
		if(start == N) {
			if (sum_cal <= limit) {
				max_score = Math.max(max_score, sum_score);
			}
			return; 
		}
		// i번째 재료 포함 
		backtracking(start+1, sum_score+combo[start][0], sum_cal+combo[start][1], combo, N, limit);
		// i번째 재료 포함x 
		backtracking(start+1, sum_score, sum_cal, combo, N, limit);
	}
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(); 
		StringTokenizer st = null;
		
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int limit = Integer.parseInt(st.nextToken());
			
			// 재료 배열 
			int[][] combo = new int[N][2];  // (점수, 칼로리) 
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				combo[i][0] = Integer.parseInt(st.nextToken());
				combo[i][1] = Integer.parseInt(st.nextToken());
			}
			
			// limit을 안 넘는 선에서, 최대 점수의 조합을 찾는다. 
			// 백트래킹 -> 선택 or not 선택의 경우 
			backtracking(0, 0, 0, combo, N, limit);
//			System.out.println(max_score);
			sb.append("#").append(tc).append(" ").append(max_score).append("\n");
			max_score = 0; 
		}
		System.out.println(sb.toString());
	}

}
