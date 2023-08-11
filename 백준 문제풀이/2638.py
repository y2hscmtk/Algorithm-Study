# https://www.acmicpc.net/problem/2638
'''
0,0에서 탐색 시작
0만나면 방문처리 후 넘어가기
1(치즈)만나면 상하좌우의 0에 대해서 다시 탐색하여 끝방향(밖의 공기인지 판별하기 위해)인지 확인
끝 방향에 도달하는 0의 개수가 2개 이상이라면 방문처리 후 빈공간 처리(녹음)
'''
from collections import deque
N, M = map(int, input().split())
# 현재 치즈 상태(1은 치즈, 0은 빈 공간)
cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 치즈가 모두 녹았는지 확인
def isFinish():
    for array in cheese:
        # 아직 안 녹은 치즈가 남아 있다면
        if 1 in array:
            return False
    # 다 녹았다면(1이 한개도 없다면)
    return True


# 디버깅용 치즈 상태 출력
def print_cheese():
    for array in cheese:
        print(*array)


# 외부 공기를 만나는지 확인
# 해당 좌표에서부터 bfs를 수행하여 테두리 끝에 도달하였는지 확인
def isOutAir(s, e):
    queue = deque()
    queue.append([s, e])
    visited = [[False]*M for _ in range(N)]
    visited[s][e] = True
    while queue:
        x, y = queue.popleft()
        # 도달한 좌표가 각 테두리 값에 해당하는지 확인
        if x == 0 or x == N-1 or y == 0 or y == M-1:
            return True  # 테두리에 도착하였다 => 외부 공기다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고, 방문하지 않은 좌표인지 확인
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if cheese[nx][ny] == 0:  # 0인지 확인
                    visited[nx][ny] = True  # 방문처리
                    queue.append([nx, ny])
    # 테두리에 도달하지 못한채로 bfs가 종료됨 => 내부 공기다
    return False


# 치즈 녹이기(0,0에서부터)
def melt():
    global cheese
    queue = deque()
    melt_cheese = deque()  # 탐색이 끝난 이후 녹일 치즈들
    queue.append([0, 0])
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고, 방문하지 않은 좌표인지 확인
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 공기를 만나면
                if cheese[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                # 치즈를 만나면
                elif cheese[nx][ny] == 1:
                    # 네 방향 검사
                    count = 0
                    for j in range(4):
                        cx = nx + dx[j]
                        cy = ny + dy[j]
                        # 범위를 벗어나지 않는 공기라면
                        if 0 <= cx < N and 0 <= cy < M and cheese[cx][cy] == 0:
                            # 바깥 공기인지 검사
                            if isOutAir(cx, cy):
                                count += 1
                    # 검사 결과 바깥공기와 2변 이상 접촉했다면
                    if count >= 2:
                        # 치즈 녹이기
                        melt_cheese.append([nx, ny])
                        visited[nx][ny] = True
    # 치즈들 모두 녹이기
    for x, y in melt_cheese:
        cheese[x][y] = 0


time = 0  # 정답
while True:
    # 치즈가 다 녹았다면 종료
    if isFinish():
        break
    # 아직 안 녹은 치즈가 있다면
    # 치즈 녹이기
    melt()
    time += 1  # 치즈가 녹는데 1시간이 걸림
    # 디버깅용
    # print("--------------------------")
    # print_cheese()


print(time)
