# https://www.acmicpc.net/problem/24447
'''
N개의 정점, M개의 간선으로 구성된 무방향 그래프
시작 정점은 R, 각 정점의 번호는 1~N
시작 정점의 깊이는 0, 아직 방문되지 않은 노드의 깊이는 -1로
i번 노드의 방문 순서를 ti 라고 할 때, 모든 노드에 대한 di x ti의 값을 구하라
시작 정점의 방문 순서는 1, 시작 정점에서 방문할 수 없는 노드는 0이다.
인접 정점은 오름차순으로 방문한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
N,M,R = map(int,input().split())
# (방문순서, 깊이)
visited = [[0,-1] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

def bfs(r):
    queue = deque()
    queue.append(r)
    # 시작 정점 방문처리
    t = 1
    visited[r][0] = t # 시작 정점의 방문 순서는 1
    visited[r][1] = 0 # 시작 정점의 깊이는 0
    while queue:
        x = queue.popleft()
        for nx in graph[x]: # 인접 정점들에 대하여
            if visited[nx][1] == -1: # 아직 방문하지 않은 경우
                # 방문 순서 기록
                t+=1
                visited[nx][0] = t
                # 깊이 기록
                visited[nx][1] = visited[x][1] + 1
                queue.append(nx)

# 간선 정보 입력받기
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 인접 정점은 오름차순으로 방문한다.
for i in range(N+1):
    graph[i].sort()

# R에서 탐색 시작
bfs(R) 

# 모든 정점에 대해서 di x ti의 값을 구하라
result = 0
for i in range(1,N+1):
    result += (visited[i][0] * visited[i][1])

print(result)