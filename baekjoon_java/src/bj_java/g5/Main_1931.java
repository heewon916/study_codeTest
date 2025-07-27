package bj_java.g5;

import java.util.*;
import java.io.*;

public class Main_1931 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[][] timeList = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			timeList[i] = new int[] { a, b };
		}
		// Arrays.sort(timeList, (a, b) -> Integer.compare(a[1], b[1]));
		Arrays.sort(timeList, (a, b) -> {
			if (a[1] == b[1])
				return Integer.compare(a[0], b[0]); // 끝나는 시간이 같으면 시작 시간 오름차순
			return Integer.compare(a[1], b[1]);
		});

		// for (int[] a : timeList)
		// System.out.println(Arrays.toString(a));

		int res = 0;
		int end = 0;
		for (int[] m : timeList) {
			if (end <= m[0]) {
				end = m[1];
				res++;
				// System.out.println(m[0] + " " + m[1] + " " + end + " " + res);
			}
		}
		System.out.println(res);
	}
}
