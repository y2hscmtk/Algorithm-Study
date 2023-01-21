# https://www.acmicpc.net/problem/14502

'''
연구소에 벽을 세워 안전영역의 최댓값을 구하라
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.
벽은 꼭 3개를 세워야한다.
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.
'''
'''
아이디어 : 바이러스가 퍼져나가는것은 BFS를 통해 구현(고정), 벽을 세우는것은 빈공간중 3개를 골라 바이러스가 퍼져나가는 상황을 반복하여 확인한다.
3개의 벽이 세워지는 모든 경우의 수에 대하여 안전영역을 계산하고 안전영역의 최대값을 갱신하여 최종 출력한다.
'''
import sys
import copy # 깊은 복사를 위해
from collections import deque # BFS에 사용할 덱
input = sys.stdin.readline


# 세로의 크기(n:행), 가로의 크기(m:열)
n, m = map(int, input().split())
# 연구실 정보 입력받기
laboratory = [list(map(int, input().split())) for _ in range(n)]

result = 0  # 안전영역을 저장할 배열 => 재귀호출을 통해 업데이트한다.


# 네방향으로 이동하기 위한 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 바이러스를 퍼뜨리기 위해 BFS => 2를 대상으로 상하좌우에 1이 없다면(즉 0이라면)주변으로 바이러스를 감염시킨다.
def bfs(copy_lab, x, y):
    queue = deque()  # BFS에 활용할 덱 생성
    queue.append([x, y])
    # 큐가 존재하는 동안 bfs
    while queue:
        a, b = queue.popleft()
        # 네방향으로 이동
        for i in range(4):
            mx = a + dx[i]
            my = b + dy[i]
            # 이동한 좌표가 배열의 범위를 벗어나지 않는지,해당좌표가 빈공간(0)인지 확인
            if 0 <= mx < n and 0 <= my < m and copy_lab[mx][my] == 0:
                copy_lab[mx][my] = 2  # 바이러스를 퍼뜨리고
                queue.append([mx, my])  # 해당 좌표 큐에 삽입


# 바이러스를 퍼뜨리기 위한 함수
# 벽이 설치된 깊은 복사된 배열을 탐색하여 2를 만나면 해당좌표를 기준으로 BFS를 수행한다.
def spread_virus(copy_lab):
    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 2:
                bfs(copy_lab, i, j)


# 안전지대의 크기를 계산하여 리턴
def count_safety(copy_lab):
    safe = 0  # 안전지대의 영역
    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 0:  # 안전영역을 만나면 safe 증가
                safe += 1
    return safe


# 배열을 탐색하며 0을 만나면 벽을 세우고, 벽의 개수가 3개가 되면 해당 배열을 바탕으로 BFS수행
# 1은 벽, 0은 빈공간 2는 바이러스
def make_wall(lab, wall):
    global result
    # 배열을 탐색하며 빈공간을 만나면 벽을 세우고, 벽의 개수가 3개가 넘어갔다면 BFS를 수행한다.
    for i in range(n):
        for j in range(m):
            if wall == 3:  # 벽을 3개 세우면 해당 배열을 바탕으로 바이러스 퍼뜨리기
                # 바이러스를 퍼뜨린후 안전지대를 계산하여 기존 안전지대보다 넓다면 갱신
                spread_virus(lab)
                # 안전지대의 최대값을 갱신하여 저장한다.
                result = max(result, count_safety(lab))
                return

            if lab[i][j] == 0:  # 빈공간을 만난다면 벽 세우기
                # 원본배열이 손상되지 않도록 배열을 복사
                # 연구실의 현재상태 저장 => 새롭게 새운 벽을 대상으로 BFS를 수행하기 위함
                copy_lab = copy.deepcopy(lab)
                # 벽을 세우고, 세운 벽의 좌표를 기억한채로 나머지 벽을 세워야 함 => 스택활용
                copy_lab[i][j] = 1
                # 재귀호출을 통해 벽의 좌표를 기억, 벽의 개수를 증가시켜 재귀호출
                make_wall(copy_lab, wall+1)


wall = 0
# 빈공간중 3곳이 될수 있는 모든 경우의 수에 대하여 벽을 세우고 탐색 진행
make_wall(laboratory, wall)
print(result)
