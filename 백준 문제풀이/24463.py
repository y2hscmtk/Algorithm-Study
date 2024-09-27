# https://www.acmicpc.net/problem/24463
import sys
sys.setrecursionlimit(10**4)
N,M = map(int,input().split())

hall = [] # 입구와 출구
graph = []
for i in range(N):
    row = list(input())
    for j in range(len(row)):
        if row[j] == '.': # 빈칸을 발견했을 때  
            row[j] = '@' # 아직 사용되지 않았으므로
            # 입구, 출구 파악
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                hall.append((i,j))
    graph.append(row)

sx,sy = hall[0]; ex,ey = hall[1] # 입구와 출구 좌표
def dfs(x,y):
    # 목적지에 도달하였는지 확인
    if (x,y) == (ex,ey):
        graph[x][y] = '.' # 방문처리
        # 정답 출력 후 종료
        for row in graph:
            print(''.join(row))
        sys.exit(0)
        
    # 모든 방향에 대해서 이동가능한 길이 있는지 파악
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        # 이동 가능한 좌표인지 파악
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == '@':
            graph[nx][ny] = '.' # 탐색 완료로 설정 후 dfs
            dfs(nx,ny)
            graph[nx][ny] = '@' # 백트래킹

graph[sx][sy] = '.' # 출구 사용처리
dfs(sx,sy) # 입구에서 출발
