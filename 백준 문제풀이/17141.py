# https://www.acmicpc.net/problem/17141

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
'''

import sys
import copy
from collections import deque
input = sys.stdin.readline

# nxn크기의 연구실
n, m = map(int, input().split())
# 연구실 정보 입력받기
laboratory = [list(map(int, input().split())) for _ in range(n)]
# 큐 생성
queue = deque()  # 바이러스 3개를 한번에 넣고 bfs를 돌릴것

select = 0  # 바이러스 3개를 고를때 사용
result = sys.maxsize  # 최소시간 기록용

# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 바이러스를 퍼뜨림(bfs)
def bfs(queue, laboratory):
    while queue:
        x, y = queue.popleft()
        # 네 방향에 대해 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 연구실 범위를 벗어나지 않고, 빈 공간인 경우에 대해서
            if 0 <= nx < n and 0 <= ny < n:
                # 한번도 바이러스가 놓여지지않은 공간일경우 바이러스를 퍼뜨린다.
                # 0은 빈공간 -2는 바이러스가 퍼질수 있는 공간
                if laboratory[nx][ny] == 0 or laboratory[nx][ny] == -2:
                    laboratory[nx][ny] = laboratory[x][y] + 1  # 방문처리(시간 누적)
                    queue.append([nx, ny])  # 해당 좌표 큐에 삽입


# 바이러스가 퍼지는데 걸리는 최소 시간 카운트
# 빈공간(0,-2)이 남아있다면 -1을 리턴
def count_time(laboratory):
    max_time = -1
    for floor in laboratory:
        # 아직 바이러스가 퍼지지못한 곳이 있다면 -1 리턴
        if 0 in floor:
            return -1
        elif -2 in floor:
            return -1
        # 바이러스가 다 퍼졌다면 최댓값 갱신
        else:
            # 최댓값 갱신
            max_time = max(max_time, max(floor))
    return max_time


# 바이러스 m개를 놓을 장소 정하는 함수
def select_position(laboratory, select, queue):
    global result, m
    for i in range(n):
        for j in range(n):
            if select == m:  # 바이러스를 m개를 다 골랐으면
                # 큐를 복사해서 bfs에 넘겨줘야함 => bfs에 사용되는 큐와 별개로 관리하기위해
                copy_q = copy.deepcopy(queue)
                # 바이러스 퍼뜨리기
                bfs(copy_q, laboratory)
                time = count_time(laboratory)
                # 시간을 측정할수 없는경우를 제외하고 최소시간 측정
                if time != -1:
                    result = min(result, time)
                return  # 재귀함수 종료
            else:  # 아직 3개를 고르지않은 시점에서
                if laboratory[i][j] == -2:  # 바이러스를 퍼뜨릴수 있는공간을 발견한다면
                    copy_lab = copy.deepcopy(laboratory)  # 연구실 정보 복사(원본 정보 보존)
                    copy_lab[i][j] = 1  # 바이러스를 놓을 장소로 선택
                    queue.append([i, j])  # 좌표값 기억
                    select_position(copy_lab, select+1, queue)  # 재귀호출(값 기억)
                    queue.pop()  # 마지막으로 선택한 좌표를 지워야함


# 바이러스가 퍼질수 있는 공간은 2와 0이고, 양수는 시간정보와 구별하기 어려우므로 음수로변환
for i in range(n):
    for j in range(n):
        if laboratory[i][j] == 1:
            laboratory[i][j] = -1
        elif laboratory[i][j] == 2:
            laboratory[i][j] = -2

select_position(laboratory, 0, queue)
# 최소시간을 측정할수 없을경우(result가 변경되지 않았을경우) -1, 그렇지않다면 최소시간 출력
print(-1 if result == sys.maxsize else (result-1))
