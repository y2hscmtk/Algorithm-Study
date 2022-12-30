# https://www.acmicpc.net/problem/7576

'''
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.

M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.

단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.

즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.

하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.

정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
'''
# 큐 자료구조를 쓰기위해 덱을 import
from collections import deque

queue = deque()

# bfs를 수행하기위해 함수 정의


def bfs(graph):
    global m, n
    global queue
    # 큐가 존재하는동안 탐색 시작
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for i in range(4):
            # 네 방향으로 이동
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < m:  # 영역을 벗어나지 않는지 확인
                # 안익은 토마토만 익게하면 됨
                if graph[mx][my] == 0:
                    graph[mx][my] = graph[x][y] + 1  # 토마토를 익게함
                    queue.append([mx, my])


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 그래프 탐색을 진행하며 정수 1이 익은 토마토를 의미하므로,
# 하루가 지난후 익은 토마토의 영향을 받아 익은 토마토를 2로, 2 토마토에 영향을 받은 토마토를 3토마토로 증가하여 표현한다.
# 탐색 종료이후 그래프의 최대값을 출력하면, 최소일수와 관련있을것 => 단 2차원 그래프인점을 고려하여 출력
# # 탐색 종료 이후 그래프에 0인 토마토가 존재한다면 익지 않은 토마토가 있다는 의미이므로 -1을 출력하고, 그렇지 않다면 최소일수를 출력한다.

# 네 방향을 지정하기 위함
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 정점을하나씩 방문하며 탐색 진행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 탐색할 목록에 넣어두기 => 바로 bfs를 시행하지 않고, 날짜순으로 수행하기위해 담아만 둔다.
            queue.append([i, j])

# 1인 토마토에 대해 탐색 진행
bfs(graph)

# 안 익은 토마토(0)가 있는지 탐색하기 위함
isZero = False
minDate = 0  # 토마토가 다 익는데 걸리는 최소 일수를 기록하기 위함

# 안익은 토마토의 존재유무와 최소일수 계산
for g in graph:
    # 2차원 배열에서 한 줄 씩 검사를 실시한다 => 0인 토마토가 있는지
    if 0 in g:
        isZero = True
        break
    if minDate < max(g):
        # 최소일수를 구하기 위해
        minDate = max(g)

if isZero:
    print(-1)
else:
    # 모든 토마토가 다 익으면 최소일수를 출력한다.
    print(minDate-1)  # 마지막날짜에 +1 된 값이 들어가므로 -1을 해줌
