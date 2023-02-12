# https://www.acmicpc.net/problem/16234

'''
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,

r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
'''
'''
아이디어 : 2차원 배열의 각 값에 대하여 4방향으로 인접한 정점을 대상으로 조건을 만족하는지 검사한다.
조건을 만족한다면 해당 정점을 대상으로 bfs를 수행하여 조건을 만족하는 정점들을 연합으로 삼고, bfs가 종료된후 인구이동을 실시한다.
bfs를 수행하는 횟수를 카운트하여 최종 정답으로 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# nxn 크기의 배열, 인구차이 조건 l명이상 r명 이하
n, l, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 인접한 방향에 대한 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

day = 0  # 인구이동에 걸리는 시간을 기록하기 위한 변수


def bfs(s, e):
    queue = deque()
    queue.append([s, e])

    visited[s][e] = True  # 탐색 시작정점은 방문처리
    # 연합에 포함되는 좌표들을 기록할 배열
    group = [[s, e]]
    total_people = graph[s][e]  # 연합에 포함되는 총 인구수를 계산하기 위해
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않으면서 처음방문하는 좌표를 대상으로
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 조건을 만족한다면 => 연합에 포함된다면, 삽입
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    visited[nx][ny] = True  # 방문처리
                    group.append([nx, ny])  # 연합에 해당 국가 등록
                    queue.append([nx, ny])  # 좌표 큐에 삽입

    return group  # 연합정보를 리턴


# 모든 좌표의 정점에 대해 bfs를 실시할지 여부를 계산
for m in range(n*n):
    move = False
    # 방문정보를 기록할 배열
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True  # 방문처리
                group = bfs(i, j)
                # 그룹이 한개 이상인 경우에만 인구이동
                if len(group) != 1:
                    # 연합의 총 인구수 계산
                    total_population = 0
                    for x, y in group:
                        total_population += graph[x][y]
                    # 새로운 인구 지정
                    new_population = total_population//len(group)
                    # 인구 이동
                    for x, y in group:
                        graph[x][y] = new_population
                    move = True
    if move:
        day += 1  # 하루 더하기
print(day)
