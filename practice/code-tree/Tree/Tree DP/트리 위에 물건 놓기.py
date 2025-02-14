'''
트리 위에 물건 놓기
1번부터 n번가지 n개의 정점으로 이루어진 트리 존재
트리의 몇몇 정점에 물건을 놓는다. 이때, 모든 간선에 대해 간선의 양끝 두 정점 중 적어도 하나의 정점에는 물건이 놓여져 있어야한다.
조건을 만족하기 위해 필요한 최소 물건의 개수

i의 자식노드를 c1,c2, .. ck 라고 할 때
DP[i][1] : i번째 노드에 물건을 올려놓았을 때 필요한 물건의 최소 개수
DP[i][0] : i번째 노드에 물건을 올려놓지 않았을 때 필요한 물건의 최소 개수

i에 물건을 올려놓으면 - 자식 노드는 물건을 올려놓든 올려놓지 않든 상관이 없다.
DP[i][1] = min(DP[c1][0], DP[c1][1]) + min(DP[c2][0], DP[c2][1]) + .. + min(DP[ck][0], DP[ck][1])
i에 물건을 올려놓지 않으면 - 자식 노드는 반드시 물건을 올려놓아야 한다.
DP[i][0] = DP[c1][1] + DP[c2][1] + .. + DP[ck][1] 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)
INT_MAX = float('inf')
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)

for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

dp = [[INT_MAX for _ in range(2)] for _ in range(n+1)]

def dfs(root):
    # 자식 방문 처리
    for node in graph[root]:
        if not visited[node]:
            visited[node] = True
            parent[node] = root
            dfs(node)
    
    # 퇴각 하기 전, 자식들을 순회하며 dp[root] 갱신
    # 초기값 설정
    dp[root][0] = 0
    dp[root][1] = 1 # 물건을 놓는 경우이므로, 시작값 1

    # 현재 정점의 자식 노드 모두 방문
    for node in graph[root]:
        # node가 root의 자식이 아니라면 패스 - 부모를 방문하는 경우 방지(순환 방지)
        if parent[node] != root:
            continue

        # 1. root에 물건을 놓는 경우
        dp[root][1] += min(dp[node][0], dp[node][1])
        # 2. root에 물건을 놓지 않는 경우
        dp[root][0] += dp[node][1]


visited[1] = True # 시작 정점 방문 처리
dfs(1)    

print(min(dp[1]))