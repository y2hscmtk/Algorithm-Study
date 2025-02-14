'''
트리는 특정 두 정점을 고르면, 두 정점 사이를 연결하는 경로는 유지되는 성질이 존재
트리의 지름 : 각 간선에 가중치가 있는 트리 정보가 주어질 때, 모든 정점 쌍에 대한 거리 중 가장 긴 경로

특정 노드를 루트 노드로 할 때, 가장 멀리 떨어진 노드 x 탐색
이후 노드 x를 루트 노드로 할 때, 가장 멀리 떨어진 노드를 구하면 지름이 된다.
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(n-1):
    s,e,l = map(int,input().split())
    graph[s].append((e,l))
    graph[e].append((s,l))
    
# 현재 정점에서 모든 정점까지 가장 멀리 떨어진 정점 계산
def dfs(curr_node):
    for node,l in graph[curr_node]:
        if visited[node] == -1:
            visited[node] = visited[curr_node] + l
            dfs(node)

visited[1] = 0
dfs(1) # 임의의 정점 1에서 탐색 했을 때, 가장 멀리 떨어진 정점 파악

# 가장 멀리 떨어진 정점이 몇번인지 파악
max_length,target = 0,0
for i in range(1,n+1):
    if max_length <= visited[i]:
        max_length = visited[i]
        target = i

visited = [-1]*(n+1)
visited[target] = 0
dfs(target)

result = 0
for i in range(1,n+1):
    result = max(result, visited[i])

print(result)