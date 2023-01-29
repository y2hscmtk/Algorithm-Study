# https://www.acmicpc.net/problem/7562

'''
체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''

'''
BFS를 이용하여 나이트가 이동할수 있는 경로에 대해 탐색을 진행

0,0/ 0,1/ 0,2/ 0,3/ 0,4
1,0/ 1,1/ 1,2/ 1,3/ 1,4
2,0/ 2,1/ 2,2/ 2,3/ 2,4
3,0/ 3,1/ 3,2/ 3,3/ 3,4
4,0/ 4,1/ 4,2/ 4,3/ 4,4

'''
from collections import deque
t = int(input())

# 나이트가 이동할수 있는 경로
# 위의 표에서 (2,2)위치에 있다고 가정할때 8가지의 이동경로 발생
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(sx, sy, fx, fy, board, l):
    queue = deque()
    queue.append([sx, sy])  # 시작 위치 삽입
    while queue:
        x, y = queue.popleft()
        # 목적지에 도달하였다면 탐색 종료
        if x == fx and y == fy:
            return board[fx][fy]
        # 나이트가 이동 가능한 8가지 방향에 대해 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어니지 않고, 방문하지 않은 경우에 대해서
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1  # 이동경로 누적 저장
                queue.append([nx, ny])  # 큐에 좌표 삽입


for i in range(t):
    l = int(input())  # 체스판 한변의 길이
    # 빈 체스판 생성 => 이곳에서 bfs를 수행하여, 이동거리를 누적시켜 기록한다.
    board = [[0]*l for i in range(l)]  # lxl크기의 2차원 배열 생성
    sx, sy = map(int, input().split())  # 탐색 시작 위치(현재 나이트 위치) start
    fx, fy = map(int, input().split())  # 나이트가 이동하려고 하는 위치 final
    print(bfs(sx, sy, fx, fy, board, l))  # 탐색결과 출력
