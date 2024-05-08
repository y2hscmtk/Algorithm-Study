# https://www.acmicpc.net/problem/1405
'''
같은 위치를 다시 방문하는지 안하는지 확인해야함
로봇은 최대 14번 이동하므로, 로봇이 정중앙에 있다고 가정했을 때 29 x 29 크기의 배열을 준비하면 될 듯
'''
import sys
input = sys.stdin.readline
N,a,b,c,d = map(int,input().split()) # N번 이동, 동 서 남 북 확률
# 동 서 남 북
p = [a/100,b/100,c/100,d/100] # 각 방향으로 이동할 확률
dx = [1,-1,0,0] 
dy = [0,0,1,-1]
visited = [[False]*(2*N+1) for _ in range(2*N+1)]
result = 0 # 정답 확률
def dfs(x,y,depth,percentage):
    global result
    if depth == N: # 로봇 이동 종료
        result += percentage
        return
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        curr_p = p[i] # 현재 방향로 이동할 확률
        # 로봇의 경로를 단순하게 만들기 위해서는 갔던 장소는 다시 가지 않아야 한다.
        if 0<=nx<(2*N+1) and 0<=ny<(2*N+1) and not visited[nx][ny]:
            visited[nx][ny] = True # 방문처리
            dfs(nx,ny,depth+1,percentage*curr_p)
            visited[nx][ny] = False # 백트래킹
# 로봇의 시작 위치는 정 중앙
visited[N][N] = True
dfs(N,N,0,1)
print(result)