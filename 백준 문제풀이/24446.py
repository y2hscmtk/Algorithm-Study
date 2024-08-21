# https://www.acmicpc.net/problem/24446
'''
N개의 정점, M개의 간선으로 구성된 무방향 그래프
시작 정점은 R, 각 정점의 번호는 1~N
시작 정점의 깊이는 0, 아직 방문되지 않은 노드의 깊이는 -1로 출력
'''
from collections import deque

def bfs(r):
    queue = deque()
    queue.append(r)
    while queue:
        x = queue.popleft()
        # 인접 정점에 대해서
        for nx in graph[x]:
            if visited[nx] == -1: # 아직 방문하지 않은 경우
                visited[nx] = visited[x] + 1 # 방문한 깊이 표시
                queue.append(nx) # 큐 삽입

N,M,R = map(int,input().split())
visited = [-1 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

# 간선 정보 입력받기
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited[R] = 0
bfs(R) # 시작 정점은 R

for i in range(1,N+1):
    print(visited[i])