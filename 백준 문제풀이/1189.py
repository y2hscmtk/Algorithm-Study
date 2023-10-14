# https://www.acmicpc.net/problem/1189
'''
T인 부분은 방문할 수 없다.
한번 방문한 곳은 다시 방문하지 않는다.
거리가 K인 경우의 가지수
'''
R,C,K = map(int,input().split())
graph = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)] # 방문정보
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0

# dfs
def dfs(i,j):
    global result
    # 만약 목적지에 도달하였다면
    if (i,j) == (0,C-1):
        # 그리고 K만큼의 거리가 들었다면
        if visited[i][j] == K:
            result += 1 # 정답 경우의 수 추가
        return # dfs 종료
    # 해당 좌표에서의 모든 인접 좌표에 대해
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] != 'T' and visited[nx][ny]==0:
                visited[nx][ny] = visited[i][j] + 1 # 방문처리
                dfs(nx,ny)
                visited[nx][ny] = 0 # 백트래킹

# 최초 탐색 시작 위치는 왼쪽 아래
visited[R-1][0] = 1 # 시작 좌표의 거리는 1로 설정
dfs(R-1,0)
print(result)
