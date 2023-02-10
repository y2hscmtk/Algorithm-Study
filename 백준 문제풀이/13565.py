# https://www.acmicpc.net/problem/13565

'''
인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다. 

이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다. 편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다. 

또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다. 

전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 

바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.
'''
'''
아래쪽까지 도달하는것이 목표이므로, BFS를 실시하여 가장 바닥까지 도달하였다면 탐색을 중단한다.
맨 윗줄에서 0인 좌표를 대상으로 bfs를 진행하고 만약 맨 윗줄에 0인 좌표가 없다면 전기가 통할수 없으므로 BFS없이 NO 출력
'''
import sys
from collections import deque
m, n = map(int, input().split())

graph = [list(input()) for _ in range(m)]

# 방문정보를 표현할 배열
visited = [[False]*n for _ in range(m)]

# 네가지 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s, e):
    queue = deque()
    queue.append([s, e])
    visited[s][e] = True  # 시작 좌표 방문처리
    while queue:
        x, y = queue.popleft()
        # 목적지에 도달하였다면
        if x == m-1:  # 가장 아래칸에 도달하였다면
            return True  # 탐색 성공의 의미로 True 리턴
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않고, 아직 방문하지 않은 좌표에 대해서만
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == '0':  # 전기가 통하는 영역으로만 탐색 수행
                    visited[nx][ny] = True  # 방문처리
                    queue.append([nx, ny])  # 해당 좌표 삽입
    # 탐색 결과 목적지에 도달하지 못하였다면 실패의 의미로 False리턴
    return False


# 입력받은 배열을 탐색하며 맨 윗쪽에 '0'인 공간을 찾으면 해당 좌표에 대해 bfs수행
# 만약 맨 윗줄에 '0'인 공간이 없다면 전기가 통하지 않는 물질이므로 bfs없이 "NO"출력
for i in range(n):
    if graph[0][i] == '0':
        if bfs(0, i):
            print("YES")
            sys.exit(0)  # 프로그램 종료
print("NO")
