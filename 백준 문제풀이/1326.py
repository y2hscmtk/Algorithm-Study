# https://www.acmicpc.net/problem/1326
from collections import deque

n = int(input())
data = list(map(int, input().split()))
visited = [-1]*n
a, b = map(int, input().split())


# a에서 b까지 가는데 걸리는 최소횟수
# i번째 노드에서 data[i]안의 수의 배수만큼 한번에 이동 가능
def bfs(a):
    queue = deque()
    queue.append(a-1)  # a에서 탐색 시작
    visited[a-1] = 0  # 방문처리
    while queue:
        now = queue.popleft()
        # 목적지에 도달했는지 확인
        if now == b-1:
            return visited[now]
        for i in range(1, n):
            nx = now + data[now]*i  # data[now]의 i배수만큼 이동 가능(오른쪽)
            # 영역을 넘어서지 않는지 확인
            if 0 <= nx < n and visited[nx] == -1:
                visited[nx] = visited[now] + 1  # 방문처리
                queue.append(nx)
            nx = now - data[now]*i  # data[now]의 i배수만큼 이동 가능(왼쪽)
            # 영역을 넘어서지 않는지 확인
            if 0 <= nx < n and visited[nx] == -1:
                visited[nx] = visited[now] + 1  # 방문처리
                queue.append(nx)
    # 목적지에 도달하지 못했다면 -1
    return -1


print(bfs(a))
