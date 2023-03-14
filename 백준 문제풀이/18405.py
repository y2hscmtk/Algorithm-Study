# https://www.acmicpc.net/problem/18405
'''
NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 

모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 

단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 

또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 

만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 

이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 

서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다.

이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.
'''
'''
아이디어 : 2차원 배열을 탐색하고, 우선순위 큐를 이용하여 바이러스 우선순위에 맞춰, 데이터를 삽입해두고 우선순위에 맞춰서 바이러스 전염을 수행한다.
s초가 지난후, (x,y) 좌표를 출력한다. => 우선순위 큐를 이용할경우 알수없는 이유로 23퍼정도에서 오류 발생
'''
from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

# 방향 벡터 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 큐로 사용할 리스트 생성
queue = []
# 전체 바이러스의 위치를 파악하여 우선순위에 맞춰, 우선순위 큐에 삽입
for i in range(n):
    for j in range(n):
        # 만약 바이러스가 존재한다면 우선순위 큐에 우선순위에 맞춰 삽입
        if graph[i][j] != 0:
            # 첫번째 요소에 바이러스의 종류를 넣어 기준으로 삽입
            queue.append([graph[i][j], i, j, 0])

# 첫번째 요소를 기준으로 정렬(바이러스 종류에 따라 우선순위가 다르므로)
queue.sort()

queue = deque(queue)

# bfs 수행
while queue:
    virus_type, a, b, time = queue.popleft()

    # 만약 time이 s초가 되었다면 반복 종료
    if time == s:
        break

    # 네 가지 방향으로 바이러스 퍼뜨리기
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        # 영역을 벗어나지 않으면서, 처음 방문하는 값인 경우 반복 수행
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus_type  # 바이러스 전염
            # 이동한 바이러스의 좌표 큐에 삽입, 삽입시 시간정보를 +1해서 저장
            queue.append([virus_type, nx, ny, time+1])

# s초가 지난후의 (x,y) 좌표를 출력한다. => 1,1부터 시작하므로 +1,+1을 해줘야함
print(graph[x-1][y-1])
