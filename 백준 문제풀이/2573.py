# https://www.acmicpc.net/problem/2573

'''
지구 온난화로 인하여 북극의 빙산이 녹고 있다.
빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자.
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 
빙산 이외의 바다에 해당되는 칸에는 0이 저장된다.

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
'''

'''
아이디어 : 빙하가 동시에 녹아야하므로, 배열을 검사해서 빙하를 만났을때 상하좌우의 바다의 수를 계산하여 좌표와 함께 배열에 임시로 삽입한다.
탐색이 종료된 이후 동시에 빙하를 녹여주고(반복문 사용) 이후 bfs를 하여 빙하의 개수가 2개가 되었는지 확인한다.
빙하의 개수가 2개 이상으로 분리되었다면, 걸린 시간을 출력하고 그렇지않다면 1년을 추가한후 위의 과정을 반복한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# 행,열
n, m = map(int, input().split())
# 빙하 정보 입력받기
iceberg = [list(map(int, input().split())) for _ in range(n)]

year = 0  # 빙하가 2덩이 이상으로 분리되려면 얼마나 걸리는지를 기록
group = 0  # 빙하의 그룹(덩어리 수)를 카운트하기 위함

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# bfs(빙하 그룹 카운트용)
def bfs(a, b):
    global visited, n, m, iceberg
    queue = deque()
    queue.append([a, b])  # 탐색 시작 좌표 큐에 삽입
    visited[a][b] = True  # 시작좌표 방문처리
    while queue:
        x, y = queue.popleft()
        # 네 방향 검사 (동서남북으로 붙어있는 칸들은 서로 연결되어 있는것으로 간주)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 빙산배열의 범위를 벗어나지않으면서, 아직 방문하지 않은 빙하 방문
            if 0 <= nx < n and 0 <= ny < m:
                if iceberg[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True  # 방문처리
                    queue.append([nx, ny])


# 빙하가 다 녹거나, 두 덩어리 이상으로 분열될때까지 반복
while True:
    allMelt = True  # 빙하가 다 녹았을때를 나타내기 위해
    # 빙하가 다 녹았는데,두 덩어리 이상으로 분리되지 않을경우 0을 출력
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:  # 하나라도 빙하가 존재한다면
                allMelt = False
                break  # 반복종료

    if allMelt:  # 빙하가 다 녹았다면
        print(0)  # 0 출력후 프로그램 종료
        break

    # 빙하가 두덩어리 이상으로 되었는지 검사
    # 시작부터 두 덩어리 이상일수 있으므로, 빙하를 녹이기전에 먼저 검사한다.
    # 방문정보를 기록할 배열, bfs에 사용
    visited = [[False]*m for _ in range(n)]
    # 빙하 그룹 카운트
    count = 0
    for i in range(0, n):
        for j in range(0, m):
            # 빙하를 만났는데,방문한적이 없다면 bfs수행하고, count수를 증가
            if iceberg[i][j] != 0 and not visited[i][j]:
                count += 1
                # 빙하가 두 덩어리 이상으로 나뉘어졌다면 year출력하고 프로그램 종료
                if count >= 2:
                    print(year)
                    sys.exit(0)
                bfs(i, j)  # 아직 한덩어리밖에 탐색이 되지 않았다면 bfs수행

    # 녹일 빙하에 대한 좌표를 저장할 배열
    melt_array = []  # i,j,n => iceberg[i][j]의 값을 n만큼 감소시킨다.(0이하로는 떨어지지 않도록)
    # 빙하의 인접한 바다 개수 카운트(바다 : 0)
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:  # 빙하를 만나면 상하좌우의 바다 개수 검사
                count = 0  # 바다 개수를 저장
                # 네 방향에 대해 검사
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    # 빙산배열의 범위를 벗어나지않으면서 해당 좌표가 바다라면
                    if 0 <= ni < n and 0 <= nj < m and iceberg[ni][nj] == 0:
                        count += 1  # 바다개수 증가
                # 네방향 탐색이 끝난 후 배열에 삽입
                melt_array.append([i, j, count])

    # 빙하 녹이기 시작
    for x, y, d in melt_array:
        iceberg[x][y] -= d
        # 빙하는 0이하로 녹지않는다.
        if iceberg[x][y] < 0:
            iceberg[x][y] = 0

    year += 1  # 빙하는 1년마다 녹는다.
