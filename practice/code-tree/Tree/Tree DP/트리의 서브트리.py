import sys
sys.setrecursionlimit(100000)
n, r, q = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
U = [int(input()) for _ in range(q)]

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)
dp = [0 for _ in range(n+1)]
 
for x,y in edges:
    graph[x].append(y)
    graph[y].append(x)

def dfs(root):
    # 리프노드까지 도달
    for node in graph[root]:
        if not visited[node]:
            visited[node] = True
            parent[node] = root # 부모 설정
            dfs(node)
    
    dp[root] = 1 # 자기 자신

    # 모든 자식에 대해서 - 부모는 방문하지 말아야 함
    for node in graph[root]:
        if parent[node] != root: # 서브트리의 부모가 아닌 경우
            continue
        dp[root] += dp[node] # 자식 노드의 개수 취합


visited[r] = True
dfs(r)

for node in U: # 조사할 모든 정점에 대해서
    print(dp[node]) # 자식 노드 개수 반환