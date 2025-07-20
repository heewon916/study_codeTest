package d3;

import java.io.*;
import java.util.*;

public class Solution_1289 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = null; 
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			String input = br.readLine(); // 0011 
			int count = 0;
//			char prev = input.charAt(0); 
			// 틀렸던 부분: 입력의 첫 글자가 '1'인 경우 -> 000..에서 바로 바꿔야 하는 상황이 카운트 되지 않음 
			// 예시: 100의 경우 -> 초기메모리: 000 이면, 첫 자리부터 바꿔줘야 함. 근데 나는 2번째 자리부터 바꿔야 하는지만 체크함.
			char prev = '0';
			for(int j=0; j<input.length(); j++) {
				if(input.charAt(j) != prev) {
					count += 1; 
				}
//				System.out.println("at " + j + ",t=" + t + " target[j]=" + target.charAt(j) + " " +count);
				prev = input.charAt(j); // t는 j-1 위치 
				
			}
//			System.out.println(input + " " + count);
			sb.append("#").append(tc).append(" ").append(count);
			System.out.println(sb.toString());
			sb.setLength(0);
		}
		
		
	}

}
