# https://www.acmicpc.net/problem/2206

'''
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 

1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 

최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
'''

'''
아이디어1
입력받은 2차원배열을 복사한후, 임의의 벽을 선택하여 제거하고 최단거리 알고리즘을 돌린다.
모든 벽에 대하여 위의 과정을 반복하며 최단거리를 업데이트하고 결과를 출력한다.
'''
import copy # 깊은 복사용
from collections import deque
import sys
n, m = map(int, input().split())

graph = [list(map(int, input())) for i in range(n)]  # 미로를 담을 그래프

# 오른쪽,아래쪽,왼쪽,위쪽 순으로 탐색
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# BFS를 이용하여 인덱스의 값을 늘려가며 탐색
# 탐색이 불가능할경우 -1을 출력
# 0일때만 이동가능 1은 벽


def bfs(copy_graph):
    queue = deque()
    # count = 2  # 시작 정점은 2로 설정(벽과 구별하기 위해) 이후 해당 값을 늘려나감
    copy_graph[0][0] = 2
    queue.append([0, 0])  # 탐색시작 정점은 0,0
    # 네 방향에 대하여 bfs
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 좌표값 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 미로의 범위를 벗어나지 않는선에서
                if copy_graph[nx][ny] == 0:  # 아직 가지 않은 길인 경우에만 이동
                    copy_graph[nx][ny] = copy_graph[x][y] + 1
                    queue.append([nx, ny])


result = 0  # 최단거리를 저장할 변수

# 2차원배열을 돌면서 임의의 벽을 골라서 벽을 부숴두고, bfs를 진행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 벽을 만나면
            copy_graph = copy.deepcopy(graph)  # 원본 그래프 복사
            copy_graph[i][j] = 0  # 벽을 허물고 탐색진행
            bfs(copy_graph)  # bfs를 진행
            # 최종 최단거리와 기존의 최단거리를 비교하여 업데이트
            result = max(result, copy_graph[n-1][m-1])

print((result-1) if (result-1) != 0 else -1)
