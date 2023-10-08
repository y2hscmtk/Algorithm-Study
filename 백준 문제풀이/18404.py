# https://www.acmicpc.net/problem/18404
from collections import deque
n, m = map(int, input().split())  # n x n 크기의 게임판, m개의 상대편 말
s, e = map(int, input().split())  # 나이트의 현재 위치


# a,b에 도달할때까지 최단으로 몇번 이동해야하는지 계산
def bfs():
    global knight_dict
    queue = deque()
    queue.append([s-1, e-1])  # 시작 지역
    visited = [[-1]*n for _ in range(n)]
    visited[s-1][e-1] = 0  # 시작 지역 방문처리
    while queue:
        x, y = queue.popleft()
        # 해당 지역에 상대편 말이 있다면 삽입
        for key in knight_dict:
            a, b = key
            if x == a and y == b:  # 해당 좌표에 상대편 말이 있다면
                knight_dict[(a, b)] = visited[x][y]  # 최단 거리 기록
                break
        for nx, ny in [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]:
            # 영역을 벗어나지 않고, 아직 방문한적 없는 지역이라면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])  # 큐에 삽입


knight_dict = {}  # 말의 위치를 저장하기 위한 배열

for _ in range(m):
    a, b = map(int, input().split())  # 상대편 말의 위치
    knight_dict[(a-1, b-1)] = -1
bfs()
for key in knight_dict:
    print(knight_dict[key], end=' ')
