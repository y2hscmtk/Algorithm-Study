# 트리 정점 거리
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dfs(curr_node,target):
    if visited[target] != -1:
        return

    for node,length in graph[curr_node]:
        if visited[node] == -1:
            visited[node] = visited[curr_node] + length
            dfs(node,target)


for _ in range(n-1):
    s,e,l = map(int,input().split())
    graph[s].append((e,l))
    graph[e].append((s,l))

for _ in range(m):
    s,e = map(int,input().split())
    visited = [-1]*(n+1)
    visited[s] = 0 # 시작 정점
    dfs(s,e) # 두 정점 사이의 거리 계산
    print(visited[e])
