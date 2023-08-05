from collections import deque

result = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(s,e):
    global result
    queue = deque()
    queue.append([s,e])
    visited = [[False]*m for _ in range(n)]
    visited[s][e] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == "X":
                    continue # 벽인 경우, 더이상 탐색 불가
                elif graph[nx][ny] == "P": # 사람을 만나면
                    result += 1 # 사람 한명 만났음
                visited[nx][ny] = True
                queue.append([nx,ny])


n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i,j)


print("TT") if result == 0 else print(result)
