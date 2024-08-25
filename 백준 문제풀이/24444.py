# https://www.acmicpc.net/problem/24444
'''
N개의 정점과 M개의 노드, 정점 번호는 1번부터 N번까지
정점 R에서부터 bfs수행
인접 정점은 오름차순으로 방문
'''
from collections import deque
import sys
input = sys.stdin.readline
N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]

def bfs(r):
    turn = 1
    visited[r] = turn # 시작 정점 방문처리
    queue = deque()
    queue.append(r)
    turn+=1
    while queue:
        x = queue.popleft()
        # 인접 정점들에 대해서
        for node in sorted(graph[x]): # 인접정점은 오름차순으로 방문함
            if visited[node] == 0: # 아직 방문하지 않은 경우
                visited[node] = turn # 방문처리, 방문 순서 기록
                turn+=1
                queue.append(node)

# 간선 정보
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# bfs 수행
bfs(R)

for i in range(1,N+1):
    print(visited[i])