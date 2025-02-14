'''
'처음'으로 자식이 2개 이상 있는 노드는 중앙 노드

중앙 노드를 루트로 한는 서브트리 중, 각 서브트리의 크기(포함된 정점의 개수)를 구한 뒤, 최대값 - 최소값 구하기
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

central_node = 0 # 중앙 노드
n,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dp = [0]*(n+1)
max_count = 0; min_count = n


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def find_central_node(root):
    global central_node

    # 자식 노드의 개수는 edge의 개수 - 1 (하나는 부모와 연결되어 있기 때문)
    child = len(graph[root]) - 1

    # 루트 노드는 +1 (부모가 없으므로)
    if root == r:
        child += 1

    # 최초로 자식노드가 2개 이상인 경우 중앙 노드
    if child >= 2 and central_node == 0:
        central_node = root
    
    # 중앙 노드가 없는 상태로 리프노트로 끝났다면 리프노드가 중앙 노드
    if child == 0 and central_node == 0:
        central_node = root
    
    for node in graph[root]:
        if visited[node]:
            continue
        
        visited[node] = True
        find_central_node(node)


def dfs(root):
    dp[root] = 1 # 초기값 설정

    # 자식 노드 순차적 방문
    for node in graph[root]:
        if visited[node]:
            continue

        visited[node] = True
        dfs(node)
        
        dp[root] += dp[node]

visited[r] = True
find_central_node(r)

# visited 정보 초기화
visited = [False]*(n+1)

visited[central_node] = True
dfs(central_node)

# 중앙 노드의 서브트리를 기준으로
for node in graph[central_node]:
    max_count = max(max_count, dp[node])
    min_count = min(min_count, dp[node])

print(max_count-min_count)