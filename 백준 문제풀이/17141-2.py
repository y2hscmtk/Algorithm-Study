# # https://www.acmicpc.net/problem/17141

'''
승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.

일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.

연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

입력
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 

10보다 작거나 같은 자연수이다.

출력
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
'''

'''
아이디어1
배열을 순회하면서 바이러스를 놓을수 있는곳(2)중 3개를 임의로 올라 모든경우의수에 대하여(브루트포스) 바이러스를 퍼뜨리고 최소시간(배열에서의 max)를 비교하여 출력

두번째 시도 : 아이디어는 동일, 시간복잡도 문제를 해결하기위해 deepcopy를 사용하지않고, 경우의수 탐색시, itertools라이브러리의 combination을 이용
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 연구실은 nxn크기
n, m = map(int, input().split())
# 연구실 정보 입력받기
lab = [list(map(int, input().split())) for _ in range(n)]
# 연구실에서 바이러스를 놓을수 있는 자리(2)를 탐색하여 virus배열에 삽입
virus = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i, j])  # 바이러스를 놓을수 있는 장소에 대한 정보를 사전에 기록

# 최소시간을 저장하기 위한 변수
result = sys.maxsize

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 바이러스를 퍼뜨리는 과정(bfs)
def bfs(virus_list):
    time = 0
    # 큐에 바이러스 위치들 삽입하여 생성
    queue = deque(virus_list)
    # visted배열 초기화
    # visted배열을 새롭게 생성하고 사용함으로서, lab배열의 값을 보존한채로 bfs수행 가능
    visited = [[-1 for i in range(n)] for j in range(n)]
    # visited배열의 값 초기화
    for x, y in queue:
        visited[x][y] = 0  # 초기값 0으로 설정 => 값을 누적시켜 시간을 늘려주기 위함
    while queue:  # 큐에 데이터가 존재하는 동안 반복
        x, y = queue.popleft()
        # 네 방향에 대해 탐색 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고, 처음 방문하는 좌표에 한해서
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 연구실의 해당좌표가 벽이 아니라면(바이러스가 퍼질수 있는 위치라면)
                if lab[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1  # 시간 누적(방문처리)
                    queue.append([nx, ny])  # 좌표 큐에 삽입
                    time = max(time, visited[nx][ny])  # 최대시간 갱신
    # 바이러스가 모두 퍼졌는지 검사하여 최소시간 리턴
    # 벽이 아닌데, 방문하지 않았다면 해당  좌표는 방문실패
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and visited[i][j] == -1:
                return -1  # 탐색 실패
    # 탐색 성공시 time리턴
    return time


# combination을 이용하여 virus리스트에서 임의의 m개 바이러스를 골라 리스트 생성
for virus_position in combinations(virus, m):
    # 생성한 리스트를 bfs에 넘겨주어 bfs수행
    time = bfs(virus_position)
    # 탐색 실패가 아닐경우에 result갱신
    if time != -1:
        result = min(result, time)

# 탐색에 실패하지 않았다면 result출력, 실패했다면 -1 출력
print(-1 if result == sys.maxsize else result)
