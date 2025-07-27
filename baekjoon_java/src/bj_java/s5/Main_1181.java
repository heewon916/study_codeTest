package bj_java.s5;
import java.io.*;
import java.util.*; 

public class Main_1181 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null; 
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		
		// 중복 제거를 위한 Set
		Set<String> set = new HashSet<>(); 
		for(int i=0; i<N; i++)
			set.add(br.readLine());
		
		// List로 변환해서 정렬 
		List<String> list = new ArrayList<>(set);
		
		// 정렬 기준 적용
		Collections.sort(list, new Comparator<String>(){
			public int compare(String s1, String s2) {
				if(s1.length() != s2.length()) {
					return s1.length() - s2.length(); 
				}
				return s1.compareTo(s2);
			}
		});
		for(String s: list) {
			System.out.println(s);
		}
//		Arrays.sort(arr, new Comparator<String>() {
//			public int compare(String s1, String s2) {
//				return Integer.compare(s1.length(), s2.length());
//			}
//		});
		
		
		
		
	}

}
