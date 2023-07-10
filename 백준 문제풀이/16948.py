# https://www.acmicpc.net/problem/16948
from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())


def bfs(r1, c1):
    queue = deque()
    queue.append([r1, c1])
    visited = [[0]*n for _ in range(n)]
    while queue:
        r, c = queue.popleft()
        # 목적지에 도달하였다면
        if r == r2 and c == c2:
            return visited[r][c]
        for nr, nc in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
    return -1


print(bfs(r1, c1))
