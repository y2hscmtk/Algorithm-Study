from collections import deque
r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(13)]

visited = [[False]*c for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

Q = deque()


def bfs(s, e):
    queue = deque()
    queue.append([s, e])
    Q.append([s, e])
    visited[s][e] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if cheese[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    Q.append([nx, ny])


for i in range(r):
    for j in range(c):
        if cheese[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

# count = 0
# for i in range(r):
#     for j in range(c):
#         if cheese[i][j] == 1:
#             count += 1

Q = list(Q)
Q.sort()

print(Q)
