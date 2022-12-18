# https://www.acmicpc.net/problem/2178

'''
백준 2178번 미로찾기

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 

이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 

한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''

from collections import deque

n, m = map(int, input().split())

graph = []  # 미로를 담을 그래프

# 지도 정보 입력받기
for i in range(n):
    graph.append(list(map(int, input())))

# (1,1)에서 (n,m)으로 이동하는것이 목표, 이동할때 지나야하는 최소의 칸의 개수를 출력

# bfs로 풀이

# 네 방향에 대한 정보 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 탐색의 시작 정점 삽입

    while queue:  # 큐가 존재하는 동안
        x, y = queue.popleft()
        # 네 방향 모두에 대해 탐색 => 해당 경로가 가능성이 있다면 계속 탐색
        # 문제는 '미로'이므로 4방향중 어느 한곳에 반드시 경로가 존재할것이다.
        for i in range(4):
            # 네 방향으로의 임시 위치 nx,ny지정
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 경로가 미로의 밖에 있을경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue  # 다른방향으로 탐색 진행
            # 벽인 경우 다른방향으로
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에 대해서만 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 최종적으로 거리가 누적될수 있도록
                queue.append((nx, ny))  # 경로를 찾으면 해당 경로에서 같은 과정 반복

    # 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))
