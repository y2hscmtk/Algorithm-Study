import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.*;

public class Main {

    public static int N,M,K,count;
    public static class Node{
        int x,y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static boolean[][] visited;
    public static int[][] graph;
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};
    /**
     * 아이디어 : 처음 위치에서 마지막 위치까지 방문하지 않은 지역에 대해 Flood-Fill을 수행
     * 아직 방문하지 않은 지역을 방문할 때 로봇을 이동시킨 것으로 간주한다.
     */
    public static void bfs(int s,int e){
        Queue<Node> queue = new LinkedList<>();
        visited[s][e] = true;
        queue.offer(new Node(s, e));
        while(!queue.isEmpty()){
            Node node = queue.poll();
            int x, y, nx, ny;
            x = node.x;
            y = node.y;
            for(int i = 0; i<4;i++){
                nx = x + dx[i];
                ny = y + dy[i];
                // 범위 검사
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    // 조건 검사 => 아직 방문하지 않았으면서, 차이가 K이하인 경우에만 방문 가능
                    if(!visited[nx][ny] && Math.abs(graph[nx][ny]-graph[x][y])<=K){
                        visited[nx][ny] = true; // 방문처리
                        queue.offer(new Node(nx, ny));
                    }
                }

            }

        }

    }

    public static void run(){
        // 2차원 배열의 모든 값에 대해서 아직 방문하지 않았다면 로봇을 올려서 청소를 시작한다.
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // 아직 청소가 안된 지역이라면
                if(!visited[i][j]){
                    count++; // 로봇을 놓은 카운트 증가
                    bfs(i, j); // 청소시작
                }
            }
        }
        System.out.println(count);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        visited = new boolean[N][M];
        // 배열의 형태는 N * M 형태
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 아직 방문하지 않았다면 조건에 맞춰서 bfs를 수행하고 로봇을 놓았다는 의미로 count++;
        run();

    }

}
