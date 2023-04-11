# https://www.acmicpc.net/problem/2636
'''
0은 공기이고 1은 치즈이다.
치즈는 테두리에서부터 녹는다.
테두리가 다 녹았다면 다시 안쪽 테두리가 녹기 시작한다.
한 치즈가 녹는데는 1시간이 걸린다. 치즈가 모두 녹아 없어지는데 걸리는 시간과 마지막에 남아있는 치즈의 개수를 출력하라
'''
from collections import deque
r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s, e):
    global remain_cheese
    # 방문정보 저장용
    visited = [[False]*c for _ in range(r)]
    queue = deque()
    queue.append([s, e])
    visited[s][e] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고, 방문하지 않은 좌표에 대하여
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                # 0인 좌표(공기)를 발견하였다면 큐에 삽입하고
                if cheese[nx][ny] == 0:
                    queue.append([nx, ny])
                else:  # 테두리의 치즈를 발견하였다면(1)
                    cheese[nx][ny] = 0  # 치즈를 녹인다.
                visited[nx][ny] = True  # 방문처리
    count = 0
    # 남아있는 치즈 개수 카운트
    for i in range(r):
        for j in range(c):
            if cheese[i][j] == 1:
                count += 1

    # 남아있는 치즈의 개수가 0이 아니면 remain_cheese업데이트
    if count != 0:
        remain_cheese = count
    return count  # 남아있는 치즈 개수 리턴


# 치즈가 다 녹을때까지 0,0좌표를 기준으로 0에 대해 bfs수행
# 0이 아닌 좌표를 만나면 0으로 바꿔준다.
# bfs가 끝난후 남아있는 1의 개수를 파악하여 리턴
time = 0

remain_cheese = 0  # 남아있는 치즈의 개수
# 남아있는 치즈의 개수 계산
for i in range(r):
    for j in range(c):
        if cheese[i][j] == 1:
            remain_cheese += 1


while True:
    # bfs 수행 => 남아있는 치즈의 개수 출력
    temp = bfs(0, 0)
    time += 1  # 치즈가 다 녹는데는 1시간이 걸림

    # 만약 남아있는 치즈가 없다면
    if temp == 0:
        print(time)
        print(remain_cheese)
        break
