# https://www.acmicpc.net/problem/3187
'''
빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k' 로 나타낸다.
같은 울타리 공간 안에서
양이 더 많으면 양이 늑대를 잡아먹고
늑대가 더 많으면 늑대가 양을 잡아먹는다.
'''
'''
'.'을 만나면 인접한 모든 '.'에 대해서 탐색을 진행하며
해당 울타리 구간안의 늑대의 수와 양의 수를 계산한다.
bfs가 끝난후 더 많은쪽에서 큰 쪽을 빼고, 수를 각각 기록한다.
'''
from collections import deque
r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]

# 방문정보를 기록할 배열
visited = [[False]*c for _ in range(r)]

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


wolf_count, sheep_count = 0, 0  # 늑대와 양의 수의 최종 결과


def bfs(s, e):
    global wolf_count, sheep_count
    queue = deque()
    queue.append([s, e])
    visited[s][e] = True  # 방문처리
    wolf, sheep = 0, 0
    if graph[s][e] == 'v':
        wolf += 1
    elif graph[s][e] == 'k':
        sheep += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는지, 방문한적 없는 좌표인지 확인
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                # 울타리가 아닌지 확인
                if graph[nx][ny] != "#":
                    # 만약 양이나 늑대라면
                    if graph[nx][ny] == 'v':
                        wolf += 1
                    elif graph[nx][ny] == 'k':
                        sheep += 1
                    visited[nx][ny] = True  # 방문처리
                    queue.append([nx, ny])
    # bfs 종료 이후 늑대와 양의 차이를 계산하여 누가 잡아 먹힐것인지 계산
    if sheep > wolf:  # 양의 수가 늑대보다 많다면 늑대가 잡아먹힌다.
        wolf = 0
    else:
        sheep = 0  # 그 이외의 경우엔 양이 잡아 먹힌다.
    # 양과 늑대 수 기록
    sheep_count += sheep
    wolf_count += wolf


# 2차원 배열을 탐색하며 한번도 방문한적 없는 '.'에 대해 bfs 수행
for i in range(r):
    for j in range(c):
        # 울타리가 아닌 좌표라면(울타리 안에 .없이 동물만 있을수도 있음)
        if graph[i][j] != '#' and not visited[i][j]:
            bfs(i, j)  # bfs 수행

print(sheep_count, wolf_count)
