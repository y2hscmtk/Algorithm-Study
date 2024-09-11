# https://www.acmicpc.net/problem/18126
'''
입구에서 최대한 먼 방 구하기
'''
from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    # A번 방과 B방 사이를 연결하는 길이 길이가 C임을 의미한다.
    A,B,C = map(int,input().split())
    graph[A].append((B,C)) # A에서 B까지 오가는데 걸리는 길이가 C임을 의미한다.
    graph[B].append((A,C)) # 길은 양방향 길로 서로 오갈 수 있다.
    
# 탐색 시작은 항상 1번방부터 시작
def bfs():
    queue = deque()
    queue.append(1)
    visited = [0 for _ in range(N+1)] # 1번부터 N번까지의 방
    while queue:
        x = queue.popleft()
        for next,lenght in graph[x]: # x의 인접 정점 n을 기준으로
            if visited[next] == 0: # 아직 방문한적 없다면
                visited[next] = lenght + visited[x]
                queue.append(next)
    # visited 중에서 가장 길이가 긴 값을 반환
    return max(visited)

print(bfs())
