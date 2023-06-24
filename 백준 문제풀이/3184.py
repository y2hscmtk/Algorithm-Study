from collections import deque

result = [0, 0]

r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s, e):
    global graph, result
    sheep, wolf = 0, 0
    queue = deque()

    if graph[s][e] == 'o':
        sheep += 1
    elif graph[s][e] == 'v':
        wolf += 1

    queue.append([s, e])

    graph[s][e] = '#'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '#':
                    continue
                elif graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                graph[nx][ny] = '#'
                queue.append([nx, ny])
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    result[0] += sheep
    result[1] += wolf


for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            bfs(i, j)
print(*result)
