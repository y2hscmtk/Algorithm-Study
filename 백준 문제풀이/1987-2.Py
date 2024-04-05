# https://www.acmicpc.net/problem/1987
'''
bfs로 풀어보기
'''
import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]

def bfs():
    # 현제 좌표, 비트마스크 visited, 이동한 칸 수
    queue = deque([(0, 0, 1 << (ord(graph[0][0]) - ord('A')), 1)])
    result = 1  # 최대 이동 칸 수
    while queue:
        x, y, visited, count = queue.popleft()
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]: # 상하좌우 방향에 대해서
            if 0 <= nx < R and 0 <= ny < C:
                # 다음 칸에 있는 알파벳의 비트
                next_alpha_bit = 1 << (ord(graph[nx][ny]) - ord('A'))
                # 아직 방문하지 않은 알파벳인 경우
                if not visited & next_alpha_bit:
                    # 방문 처리 후 큐에 추가
                    queue.append((nx, ny, visited | next_alpha_bit, count + 1))
                    result = max(result, count + 1) # 최대 이동거리 갱신
    return result

print(bfs())

