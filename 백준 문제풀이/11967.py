# https://www.acmicpc.net/problem/11967
'''
문제
농부 존은 최근에 N × N개의 방이 있는 거대한 헛간을 새로 지었다. 

각 방은 (1, 1)부터 (N,N)까지 번호가 매겨져있다(2 ≤ N ≤ 100). 어둠을 무서워하는 암소 베시는 최대한 많은 방에 불을 밝히고 싶어한다.

베시는 유일하게 불이 켜져있는 방인 (1, 1)방에서 출발한다. 어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치가 달려있다. 

예를 들어, (1, 1)방에 있는 스위치로 (1, 2)방의 불을 끄고 켤 수 있다. 

베시는 불이 켜져있는 방으로만 들어갈 수 있고, 각 방에서는 상하좌우에 인접한 방으로 움직일 수 있다.

베시가 불을 켤 수 있는 방의 최대 개수를 구하시오.

입력
첫 번째 줄에는 N(2 ≤ N ≤ 100)과, M(1 ≤ M ≤ 20,000)이 정수로 주어진다.

다음 M줄에는 네 개의 정수 x, y, a, b가 주어진다. (x, y)방에서 (a, b)방의 불을 켜고 끌 수 있다는 의미이다. 

한 방에 여러개의 스위치가 있을 수 있고, 하나의 불을 조절하는 스위치 역시 여러개 있을 수 있다.

출력
베시가 불을 켤 수 있는 방의 최대 개수를 출력하시오.
'''
from collections import deque
# 첫 번째 줄에는 N(2 ≤ N ≤ 100)과, M(1 ≤ M ≤ 20,000)이 정수로 주어진다.
n, m = map(int, input().split())

# 딕셔너리 형태로 정의
switch = {}

# 상하좌우 방향벡터 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문정보 확인
visited = [[False]*n for _ in range(n)]

result = 1  # 최초의 방은 불이 켜져있으므로 1부터 시작

# 특정 방의 스위치를 작동시킨 이후, 스위치를 작동시킴으로서 새로이 방을 방문하게 될 가능성이 있으므로
# 다시 상하좌우에 대해 탐색을 진행해주면됨


def bfs():
    global result
    queue = deque()
    queue.append([0, 0])  # 베시는 유일하게 불이 켜져있는 방인 (1, 1)방에서 출발한다
    visited[0][0] = True  # 처음좌표는 방문처리

    while queue:
        x, y = queue.popleft()

        room_n = str(x) + ","+str(y)
        # 해당 방에 스위치가 존재한다면
        if room_n in switch:
            for a, b in switch[room_n]:
                # 아직 불이 안켜져있다면 => 불을 중복으로 키는 경우 방지
                if not light[a][b]:
                    # 스위치를 작동시킨다.
                    light[a][b] = True
                    result += 1  # 작동시킨 스위치 수 증가시키기
                    # 스위치를 작동시켰으므로, 한번 방문하여 이동할수 없음을 확인한 좌표일지라도
                    # 다시 이동할수 있는 수단이 생길 수 있음
                    # 따라서 이미 방문했던 곳이라면 4방향으로의 이동을 다시 한번 수행해야함
                    for i in range(4):
                        na, nb = a+dx[i], b+dy[i]
                        if 0 <= na < n and 0 <= nb < n and visited[na][nb]:
                            queue.append([na, nb])

        # 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는지, 불이 켜져 있어서 방문이 가능한 곳인지 확인
            if 0 <= nx < n and 0 <= ny < n and light[nx][ny]:
                # 불이 켜져 있다면 해당 방에 방문
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])


# 방 정보 생성
light = [[False]*n for _ in range(n)]  # 모두 불이 꺼져있다는 의미로?
# 0,0 방은 항상 켜둬야함 => 0,0에서 방문을 시작하기 때문에
light[0][0] = True


# 딕셔너리에 키 삽입하기
for _ in range(m):
    x, y, a, b = map(int, input().split())
    room_number = str(x-1)+","+str(y-1)
    # 기존에 키가 존재한다면 기존 배열에 정보를 추가하여 작성한다.
    if room_number in switch:
        switch[room_number].append([a-1, b-1])
    # 키가 존재하지 않는다면
    else:
        switch[room_number] = [[a-1, b-1]]  # 새롭게 리스트에 정보를 생성한다.

# 0,0 좌표에서 스위치 정보를 이용해 bfs 수행
bfs()
print(result)
