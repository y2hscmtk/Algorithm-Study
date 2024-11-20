# https://www.acmicpc.net/problem/15558
'''
1. visited 배열 : 이전 칸 방문 처리
2. t : 시간 기록 -> 1초마다 사라지므로 t보다 작은 칸으로 이동 불가
3. 영역 검사 - 0<=nx<N , t 조건 확인
'''
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(2)]

result = 0 # 게임 클리어 가능시
# 유저는 게임 시작시 왼쪽 줄의 1번째 칸 위에 서 있음
def bfs():
    global result
    queue = deque()
    visited = [[float('inf')]*N for _ in range(2)]
    visited[0][0] = 0 # visited[0]은 왼쪽 줄에 해당
    queue.append((0,0,0)) # 현재 라인, 현재 좌표, 시간
    while queue:
        line, x, t = queue.popleft()
        for nx in [x+1,x-1]:
            # 현재 시간보다 작은 칸으로는 이동 불가 -> 칸이 없어지므로
            if nx <= t:
                continue
            # N번째 칸을 뛰어 넘으면 성공
            if nx >= N:
                result = 1
                return
            # 안전한 칸(1)으로만 이동 가능, 
            # 해당 칸에 이동하려는 시간이 이전에 기록된 시간보다 적게 걸리는 경우에만 업데이트 가능
            if t+1 < visited[line][nx] and graph[line][nx] == 1:
                visited[line][nx] = visited[line][x] + 1
                queue.append((line,nx,t+1))
        nx = x + K
        if nx <= t:
            continue
        if nx >= N:
            result = 1
            return
        new_line = (line+1)%2
        if t+1 < visited[new_line][nx] and graph[new_line][nx] == 1: # 다른 라인으로 이동
            visited[new_line][nx] = visited[line][x] + 1
            queue.append((new_line,nx,t+1))
bfs()
print(result)