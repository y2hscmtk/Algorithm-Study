# https://www.acmicpc.net/problem/1600
from collections import deque
k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
# 1번 말처럼 이동 가능하다면 2개의 차원이 필요(0,1), 따라서 k+1개의 차원 생성
visited = [[[0]*w for _ in range(h)] for _ in range(k+1)]

# 인접한 곳으로 이동할 경우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 말 처럼 이동할 경우
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]

'''
말처럼 이동할것인지, 그냥 이동할 것인지를 적절하게 선택해야함
# 차원을 분리하여 k개의 차원을 만든다.
# 0번째 차원은 한번도 말처럼 움직여본적 없는 차원이 되고
# 1번째 차원은 말처럼 1번 움직여본 차원에 해당한다.
# 말처럼 이동가능한지 현재까지 이동한 횟수를 확인하여, 말처럼 이동 가능하다면 새로운 차원으로 이동하고
# 말처럼 이동이 불가능하다면 현재차원에서 이동한다.
# 목적지에 도착하였다면 최단이동 횟수를 출력한다.
'''


def bfs():
    queue = deque()
    queue.append([0, 0, 0])  # 탐색 시작 좌표, 현재까지 말처럼 움직인 횟수
    while queue:
        x, y, c = queue.popleft()  # c는 현재까지 말처럼 움직인 횟수
        if (x, y) == (h-1, w-1):  # 목적지에 도달하였다면
            return visited[c][x][y]  # 최소 횟수를 정답으로 리턴
        # 만약 아직 말처럼 움직 일 수 있는 상황이라면
        if c < k:
            # 말처럼 움직이기 시도
            for i in range(len(hx)):
                nx, ny = x + hx[i], y + hy[i]
                # 움직이고자 하는 위치에 장애물이 없고, 배열의 영역을 벗어나지 않는다면
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0:
                    # 또한 아직 방문한적이 없다면
                    if visited[c+1][nx][ny] == 0:
                        # c+1번째 차원의 배열로 이동하여 방문처리
                        # 이동 횟수는 이전 차원에서의 움직임 + 1
                        visited[c+1][nx][ny] = visited[c][x][y] + 1
                        queue.append([nx, ny, c+1])  # 차원 이동한 결과를 큐에 삽입
        # 말처럼 이동하는 것만이 꼭 최선의 결과를 내는것은 아니므로,
        # 말처럼 이동이 가능하다고 하더라도 인접한 곳으로의 이동은 항상 탐색해야함
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            # 움직이고자 하는 위치에 장애물이 없고, 배열의 영역을 벗어나지 않는다면
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0:
                # 또한 아직 방문한적이 없다면
                if visited[c][nx][ny] == 0:
                    # 차원은 그대로 두고(말 처럼 이동한 것이 아니기 때문에) 횟수 + 1
                    visited[c][nx][ny] = visited[c][x][y] + 1
                    queue.append([nx, ny, c])  # 현재 차원상태 그대로 큐에 삽입

    return -1  # 목적지에 도달 할 수 없다면 -1을 리턴한다.


print(bfs())
