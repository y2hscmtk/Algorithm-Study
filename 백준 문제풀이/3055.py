# https://www.acmicpc.net/problem/3055

'''
<탈출>
고슴도치(S)는 홍수(*)를 피해 비버(D)로 이동
S와 *는 돌(X)를 통과할수 없고, 상하좌우 인접한 공간으로 이동함
고슴도치가 비버에게 도착하는데 걸리는 최소시간을 구하라
고슴도치는 물이 찰 예정인 공간으로 이동할수 없다. 즉 다음 시간에 물이 찰 예정인 공간으로 고슴도치는 이동할수 없다.
'''
'''
고슴도치는 물이 찰 예정인 공간으로 이동할수 없다 => 물에 대하여 bfs를 먼저 실시하여라는 의미이지 않을까?
'''
# 비버가 굴로 이동할수 없다면 KAKTUS를 출력한다.
from collections import deque
r, c = map(int, input().split())
# 지도 정보 입력받기
graph = [list(input()) for _ in range(r)]
# 고슴도치(S), 홍수(*), 비버(D), 돌(X)

# 홍수의 위치를 저장할 배열
flood_array = []

# 고슴도치와 홍수의 위치 측정
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            # 고슴도치 초기위치 지정
            hedgehog_x, hedgehog_y = i, j
        elif graph[i][j] == '*':
            # 홍수 초기위치 지정
            flood_array.append([i, j])
        elif graph[i][j] == 'D':
            # 목적지 지정
            result_x, result_y = i, j

# 큐 생성 => 홍수가 먼저 bfs를 진행하고, 이후 고슴도치의 bfs가 진행되야함
# 순서에 유의하여 큐에 삽입
queue = deque()


# 홍수에 대한 방문정보를 저장하기 위한 배열 생성
flooded = [[False]*c for _ in range(r)]
# 홍수배열에서 데이터를 뽑아서 저장
for flood_x, flood_y in flood_array:
    flooded[flood_x][flood_y] = True  # 홍수의 시작위치는 침수되어 있어야함
    # 홍수가 먼저 탐색을 진행할수 있도록 먼저 삽입
    # 세번째 인자로 True와 False를 줘서 True이면 홍수의 움직임을 의미하도록 함
    queue.append([flood_x, flood_y, True])
# # 고슴도치에 대한 방문정보를 저장하기 위한 배열 => 시간을 누적시켜 저장함
visited = [[-1]*c for _ in range(r)]
visited[hedgehog_x][hedgehog_y] = 0  # 시작위치는 방문처리 시작위치에 도달하는데 걸린 시간 0초


# False이면 고슴도치의 움직임을 의미하도록
# 홍수에 대한 bfs가 선행되어야하므로, 고슴도치의 위치는 홍수의 위치를 모두 넣은 이후에 큐에 삽입
queue.append([hedgehog_x, hedgehog_y, False])


# 방향벡터 작성
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 홍수와, 고슴도치가 번갈아가며 이동하도록 bfs를 작성할것
def bfs(queue):
    while queue:
        x, y, isFlood = queue.popleft()
        # 움직이는 대상이 고슴도치인지 홍수인지 구별
        # 네 방향에 대해 탐색 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열의 범위를 벗어나지 않는지와, 인접좌표가 돌이 아닌경우에 대해서 이동
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 'X':
                # 움직이는 대상이 홍수일경우
                if isFlood:
                    # 이전에 방문하지 않은 정점에 대하여 flooded배열 수정
                    # 홍수는 비버의 집과 돌은 통과하지 못함
                    if not flooded[nx][ny] and graph[nx][ny] != 'D':
                        flooded[nx][ny] = True  # 침수처리
                        queue.append([nx, ny, True])  # 홍수의 좌표와, 홍수여부 큐에 삽입
                # 움직이는 대상이 고슴도치일경우
                else:
                    # 고슴도치의 위치가 목적지에 도달하였다면 정답 리턴
                    if x == result_x and y == result_y:
                        return visited[x][y]  # 방문하는데 걸린 시간 리턴
                    # 고슴도치는 침수될지역(침수된지역)으로 이동하지 못하고, 돌을 통과하지못함
                    # 또한 방문하지 않은 지역에 한해서 방문해야함
                    if not flooded[nx][ny] and visited[nx][ny] == -1:  # 아직 방문하지 않은 지역에 한해서
                        visited[nx][ny] = visited[x][y] + 1
                        # 움직이는 대상이 두더지임을 큐에 삽입
                        queue.append([nx, ny, False])
    # 비버가 도착하지 못한채 bfs가 종료되면 KAKTUS 리턴
    return "KAKTUS"


print(bfs(queue))
