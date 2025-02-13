'''
s번 정점에서 모든 정점에 '색칠'하는 것이 목표
s정점에서 특정 정점 k에 방문하면 k와 거리 d 이하인 모든 정점이 '색칠'된다.
이동해야하는 총 거리의 최소값 구하기

<풀이 참조>
특정 정점에 방문했을 떄, 거리가 d 이하인 정점은 모두 색칠 되므로
'리프노드'에서 거리가 d인 정점에 방문하면 이하 정점들은 모두 색칠됨
-> 시작 노드에서 리프노드를 정의하고, 리프노드에서 거리가 d이하인 정점까지 방문하는 거리계산
-> 이동 후 되돌아와야 하므로 거리를 2씩 더해준다.
'''
import sys
sys.setrecursionlimit(100000)
n,s,d = map(int,input().split()) # 정점의 수, 시작점 번호, 거리 d
# 트리의 각 간선이 연결하는 두 정점의 번호
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
dist = [0]*(n+1)

# 돌아온 순간에 대해서도 거리가 d이하인 정점들은 색칠처리 된다.
def dfs(root):
    # 연결된 간선을 모두 살펴보며 방문
    for node in graph[root]:
        if visited[node]:
            continue
        
        visited[node] = True
        dfs(node)

        # 가장 멀리 있는 리프노드까지의 거리 저장
        dist[root] = max(dist[root], dist[node] + 1)

visited[s] = True
dfs(s)

# dist[i] : i에서 가장 먼 리프노드까지의 거리

ans = 0
# 리프노드에서의 거리가 d 이상인 정점의 개수 카운팅
for i in range(1,n+1):
    if i == s:
        continue
    if dist[i] >= d:
        ans += 1

# 리프노드에서의 거리가 d 이상인 정점은 모두 방문했다가 되돌아와야 하므로
print(ans*2)