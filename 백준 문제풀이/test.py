# 큐를 사용하기 위함(큐보다 덱이 속도가 빠르기때문에 파이썬에서는 덱을 큐처럼 사용함)
from collections import deque


n, m = map(int, input().split())  # 섬의 행,열 개수
'''
input
5 8
1 1 1 1 1 1 1 0
1 0 0 0 0 1 1 0
1 0 1 0 1 1 1 0
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0

output
2
'''
graph = [list(map(int, input().split())) for _ in range(n)]

# 섬 => 1로 둘러쌓인 0의 집합
# 다시말해 '섬'에서 0끼리는 상하좌우로 서로 연결되어있다는 의미일것
# 그렇다면 2중 반복문을 통해 전체 배열의 인덱스에서 0을 만나면
# bfs를 통해 이어져있는 0의 집합을 그룹으로 묶고
# 이렇게 생성된 0의 집합의 상하좌우 좌표가 모두 1로 묶여져있는지 확인하여 카운트를 증가시킨다.

# 상하좌우 좌표를 탐색하기 위한 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문정보를 기록하기 위한 배열 => 같은 섬이 다시 체크되지 않기 위해
visited = [[False]*m for i in range(n)]

count = 0  # 정답(섬의 개수)

# 탐색을 시작하는 좌표


def bfs(s, e):
    global count
    queue = deque()  # 큐 생성
    queue.append([s, e])  # bfs 시작좌표 삽입
    visited[s][e] = True  # 방문처리
    # 큐가 비어있지 않은동안 반복 => bfs

    island = [[s, e]]  # 섬의 좌표를 기록하기 위해
    while queue:
        x, y = queue.popleft()
        # 네 방향에 대해 방문 시작
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고 방문한적 없는 0에 대해서
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 만약 해당 좌표가 0이라면
                if graph[nx][ny] == 0:
                    # 방문처리 후 큐에 삽입, 또한 island배열에 삽입
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    island.append([nx, ny])
                    
    # bfs 종료이후 만들어진 0의 그룹(island)이 섬인지 확인하는 작업 수행

    '''
    만약 섬이라면?
    count+=1
    '''
    print(*island)


for i in range(n):
    for j in range(m):
        # 만약 한번도 방문한적 없는 0을 발견한다면
        # bfs수행
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

print(count)
