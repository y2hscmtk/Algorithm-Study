# https://www.acmicpc.net/problem/21937
'''
X에서 탐색을 시작해서 더 이상 도달할 노드가 없을 때 까지 반복하면 될듯 => 역산
'''
from collections import deque
result = 0
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for i in range(N+1)]
for _ in range(M):
    e,s = map(int,input().split())
    graph[s].append(e) # 단방향 노드, 역산할 것이므로 거꾸로 저장
X = map(int,input().split())
# 해당 노드에서 탐색을 시작해서 더이상 도달할 수 없을 때까지 탐색 수행
def bfs(x):
    global result
    queue = deque(x)
    while queue:
        node = queue.popleft()
        # 인접 정점들 방문하면서 수행해야할 업무 카운팅
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True # 방문처리
                result += 1 # 방문노드 +1
                queue.append(n)
bfs(X)
print(result)