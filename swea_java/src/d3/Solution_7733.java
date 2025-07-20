package d3;
import java.io.*; 
import java.util.*; 

public class Solution_7733 {
	static int[] dx = {-1, 1, 0, 0}; // 상하좌우 
	static int[] dy = {0, 0, -1, 1};
	
	public static void bfs(int i, int j, int[][] mat, int[][] visited, int N) {
		Queue<int[]> q = new LinkedList<>(); 
		q.add(new int[] {i, j});
		visited[i][j] = 1; 
		while(!q.isEmpty()) {
			int[] pos = q.poll(); 
			int x = pos[0];
			int y = pos[1];
			visited[x][y] = 1;
			for(int d=0; d<4; d++) {
				int nx = x+dx[d];
				int ny = y+dy[d];
				if(0<=nx && nx <N && 0<=ny && ny<N) {
					if(visited[nx][ny] == 0) {
						visited[nx][ny] = 1; 
						q.add(new int[] {nx, ny});
					}
				}
				
			}
		}
		
	}
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(); 
		StringTokenizer st = null; 
		
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[][] mat = new int[N][N]; 
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++) {
					mat[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int max_count = 0; 
			
			// 1일차에 1인 곳을 지우고, 2일차에는 2인 곳을 지우고..
			for(int day=0; day<=100; day++) {
				int[][] visited = new int[N][N]; // 먹은 곳은 탐색이 불가능하다.
				for(int i=0; i<N; i++) {
					for(int j=0; j<N; j++) {
						if(mat[i][j] <= day) {
							visited[i][j] = -1; 
						}
					}
				}
				int temp_count = 0; 
				for(int i=0; i<N; i++) {
					for(int j=0; j<N; j++) {
						if(visited[i][j] == 0) {
							visited[i][j] = 1; 
							bfs(i, j, mat, visited, N);
							temp_count++; 
						}
					}
				}
				max_count = Math.max(max_count, temp_count);
			}
			sb.append("#").append(tc).append(" ").append(max_count).append("\n");
	
		}
		System.out.println(sb.toString());
	}

}
