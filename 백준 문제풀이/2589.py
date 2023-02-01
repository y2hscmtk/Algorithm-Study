# https://www.acmicpc.net/problem/2589

'''
각 칸은 육지(L)나 바다(W)로 표시되어 있다.
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.
육지는 한 칸을 이동하는데 1시간이 걸린다.
보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 
이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.
'''

'''
모든 육지에 대해서 bfs를 수행한뒤(브루트포스), 최댓값을 갱신한다.
'''
from collections import deque
row, col = map(int, input().split())

# 지도 입력받기
graph = [list(input()) for _ in range(row)]

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# bfs정의
def bfs(start, end):
    time = 0  # 최단 시간을 기록하기 위함
    queue = deque()
    queue.append([start, end])
    # 방문정보를 기록할 배열 생성
    visited = [[-1]*col for _ in range(row)]
    visited[start][end] = 0  # 방문처리
    while queue:
        x, y = queue.popleft()
        # 상하좌우 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지도의 범위를 벗어나지 않으면서 땅이라면
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 'L':
                # 아직 방문하지 않았다면 갱신
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    # 더 큰값으로 time값 갱신 => 최장거리에 보물이 묻혀있으므로
                    time = max(time, visited[nx][ny])
                    queue.append([nx, ny])  # 큐에 좌표 삽입
    return time


result = 0  # 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간

# 브루트포스
# 땅을 발견하면 해당위치에서 bfs를 수행하여 최장거리 업데이트
for i in range(row):
    for j in range(col):
        # 땅을 발견하면 bfs => 최장거리 리턴
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
