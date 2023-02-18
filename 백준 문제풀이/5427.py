# https://www.acmicpc.net/problem/5427

'''
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 

상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 

상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
각 지도에 @의 개수는 하나이다.
'''
'''
아이디어 : 탈출 문제의 아이디어를 적용시켜서 불을 먼저 큐에 삽입하고, 상근이의 위치를 이어서 삽입하여 돌아가며 bfs를 실시할수 있도록한다.
이 과정에서 상근이의 위치가 미로의 테두리에 도달하였다면 미로를 성공적으로 탈출한것으로 간주하고
while 반복문이 끝나는동안 리턴이 없었다면 탈출에 실패하였다는 의미로 impossible을 리턴한다.
불의 위치를 기록할 배열과, 상근이의 위치를 기록할 배열을 만들어서 각각 방문정보와 시간을 갱신하여 기록해준다.
미로를 성공적으로 탈출하였다면 상근이의 해당좌표에 대한 방문시간을 배열에서 리턴한다.
'''
from collections import deque
t = int(input())

# 방향 벡터 정의
# 동서남북 인접한 칸
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(queue):
    while queue:
        # 큐에서 데이터를 팝하고 팝된 데이터가
        # 불인지 상근이인지를 isFire를 통해 구별함
        x, y, isFire = queue.popleft()

        # 상근이에 대한 좌표이면서 목적지에 도달하였다면
        if (x == 0 or y == 0 or x == h-1 or y == w-1) and not isFire:
            return human[x][y]

        # 상하좌우 좌표에 대해 탐색 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않는지와, 해당 좌표가 벽이 아닌지 확인
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '#':
                # 만약 팝한 좌표가 불에 대한 이동이라면
                if isFire:
                    # 방문하지 않은 좌표에 대해서 방문처리
                    if not fire[nx][ny]:
                        fire[nx][ny] = True  # 해당 좌표로 불 이동
                        queue.append([nx, ny, True])
                # 만약 팝한 좌표가 상근이에 대한 이동이라면
                else:
                    # 아직 방문한적이 없는 좌표이고(-1) 해당 좌표에 불이 번져있지 않아야함
                    if human[nx][ny] == -1 and not fire[nx][ny]:
                        # 이동하는데 1시간 걸리므로 1시간 더해서 기록
                        human[nx][ny] = human[x][y] + 1
                        queue.append([nx, ny, False])  # 좌표삽입
    # 리턴없이 반복문 종료시, impossible리턴
    return -1


for _ in range(t):
    w, h = map(int, input().split())

    # 미로 입력받기
    graph = [list(input()) for _ in range(h)]

    # 불과 상근이의 초기위치를 기록하기 위한 배열
    fire_position = []
    sx, sy = 0, 0  # 상근이의 위치

    # 큐에는 불의 좌표를 먼저 기록하고, 이어서 상근이의 좌표를 기록한다.
    # @ 상근 * 불
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire_position.append([i, j])  # 불의 초기 위치 기록
            elif graph[i][j] == '@':
                sx, sy = i, j  # 상근이는 한명이므로 배열을 사용할 필요 없음

    # 상근이의 방문정보와 불의 방문정보를 저장할 배열
    human = [[-1]*w for _ in range(h)]  # 상근이의 해당좌표에 대한 시간좌표를 기록
    fire = [[False]*w for _ in range(h)]  # 해당 좌표에 불이 도달하였는지를 기록

    # 해당 테스트케이스에서 사용할 큐 생성
    queue = deque()

    # 큐에는 현재 삽입된 것이 불인지 상근이의 위치에 대한 정보인지를 알게 하기 위해 세번째 인자로 값을 준다.
    # 불의 위치를 우선적으로 삽입
    for x, y in fire_position:
        queue.append([x, y, True])  # True는 현재 큐의 값이 불이란 의미
        # 불의 최초 위치 기록
        fire[x][y] = True
    # 이어서 상근이의 위치 기록
    queue.append([sx, sy, False])  # False란 의미는 현재 값이 상근이의 좌표라는 의미
    # 상근이의 위치 방문처리
    human[sx][sy] = 0

    # 기록된 큐를 대상으로 bfs실시
    time = bfs(queue)
    print("IMPOSSIBLE" if time == -1 else time + 1)
