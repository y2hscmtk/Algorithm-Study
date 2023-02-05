# https://www.acmicpc.net/problem/17142
'''
연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 
연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 
2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
'''
'''
아이디어
활성바이러스 m개를 고르고 bfs를 수행한다. visted배열을 새롭게 생성하고, 비활성바이러스의 경우 별도로 표현해준다.
'''
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# n*n 크기의 연구실 m개의 활성 바이러스 선택
n, m = map(int, input().split())

# 연구실 정보 입력받기
# 0은 빈칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치
lab = [list(map(int, input().split())) for i in range(n)]

# 연구실 탐색하며 바이러스 위치 저장
virusPosition = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:  # 비활성바이러스의 위치
            virusPosition.append([i, j])  # 비활성바이러스 위치 기록

# 네 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# bfs 정의, 매개변수로 큐를 입력받아 동시에 바이러스 퍼뜨리기 시작
# 활성바이러스를 놓을 공간은 큐에 삽입되어 있음,
# 비활성 바이러스에 대한 구분이 필요
def bfs(queue):
    time = 0  # 시간을 기록하기 위함
    # visited배열 생성 => 시간을 누적하여 기록하기 위함
    visited = [[-1]*n for _ in range(n)]
    # 활성 바이러스 위치 기록
    for x, y in queue:
        visited[x][y] = 0  # 방문처리
    while queue:
        x, y = queue.popleft()
        # 네 방향에 대해 수행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않으면서,
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 빈공간을 방문하는 경우
                if lab[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1  # 시간 누적
                    time = max(time, visited[nx][ny])  # 시간 누적 기록
                    queue.append([nx, ny])
                # 비활성화 바이러스를 방문하는 경우
                elif lab[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y]  # 시간 누적없이 바이러스 활성화
                    time = max(time, visited[nx][ny])  # 시간 누적 기록
                    queue.append([nx, ny])

    # 탐색이 끝난 후, 빈공간이 있는지 검사
    # 벽이 아닌데, 방문하지 않았다면 해당  좌표는 방문실패
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and visited[i][j] == -1:
                return -1  # 탐색 실패
    return time


# 최저시간 기록용 변수
result = sys.maxsize


# 비활성바이러스의 위치에서 m개의 위치를 뽑아서, 모든 경우에 대해 최소시간을 업데이트
for spot in combinations(virusPosition, m):
    # 큐에 선정한 좌표 삽입
    queue = deque()
    for x, y in spot:
        queue.append([x, y])

    # 생성한 큐를 이용하여 bfs 진행
    time = bfs(queue)
    if time != -1:
        # 탐색 실패가 아닐경우에 result갱신
        result = min(result, time)


print(result if result != sys.maxsize else -1)
