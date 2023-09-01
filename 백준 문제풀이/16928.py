# https://www.acmicpc.net/problem/16928
from collections import deque, defaultdict
n, m = map(int, input().split())
# n : 사다리의 수, m : 뱀의 수
# 사다리를 만나면 위로 올라가고, 뱀을 만나면 아래로 나려간다.
# 100에 도달하면 성공
visited = [-1]*(101)  # visited[1] = 1 ; 1번칸에 1번만에 도착했다는 의미
ladder = {}  # 사다리
snake = {}  # 뱀
for _ in range(n):  # 사다리 입력받기
    s, e = map(int, input().split())
    ladder[s] = e  # s에 도달하면 e로 이동한다.
for _ in range(m):  # 뱀 입력받기
    s, e = map(int, input().split())
    snake[s] = e  # s에 도달하면 e로 이동한다.


def bfs():
    # 목표는 100에 도달하는 것
    visited[1] = 0
    queue = deque()
    queue.append(1)  # 1에서 탐색 시작
    while queue:
        now = queue.popleft()  # 현재 위치
        # 현재 위치에 사다리또는 뱀이 있어 이동해야 한다면 이동
        if now in ladder:
            visited[ladder[now]] = visited[now]  # 이동은 코스트가 0(주사위를 굴린게 아님)
            now = ladder[now]
        elif now in snake:
            visited[snake[now]] = visited[now]  # 이동은 코스트가 0(주사위를 굴린게 아님)
            now = snake[now]
        # 만약 100에 도달하였다면 정답 리턴
        if now == 100:
            return visited[100]
        # 주사위를 굴려서 1~6칸만큼 이동한다.
        for i in range(1, 7):
            next = now + i  # 다음에 이동할 칸
            # 범위를 벗어날 경우 이동하지 못함
            if next > 100:
                continue
            # 방문하지 않은 경우에 대해서만 탐색을 수행한다.
            if visited[next] == -1:
                visited[next] = visited[now] + 1  # 이동처리
                queue.append(next)


print(bfs())
