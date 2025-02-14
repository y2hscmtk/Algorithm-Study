# 트리의 부모 노드
'''
트리 : 모든 노드가 연결 되어 있고, '사이클'이 존재하지 않는 그래프를 트리라고 한다.
일반적으로 부모 - 자식 관계가 주어지지 않은 양방향 그래프의 형태로 주어지며, 
DFS를 통해 부모-자식 관계를 정의할 수 있다.

<문제>
루트 노드가 1인 트리에서 각 노드의 부모 노들르 구하는 프로그램 작성
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
# 각 노드에 대한 방문 여부 파악
visited = [False]*(n+1)
parent = [0]*(n+1) # 각 노드의 부모 노드
def dfs(curr_node):
    # 탐색 시작 노드의 연결 노드들에 대해서
    for node in graph[curr_node]:
        if not visited[node]: # 아직 방문하지 않은 노드인 경우
            visited[node] = True
            parent[node] = curr_node
            dfs(node)

visited[1] = True
dfs(1) # 루트노드가 1인 상황

for i in range(2,n+1):
    print(parent[i])