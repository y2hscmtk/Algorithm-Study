# https://www.acmicpc.net/problem/6118
from collections import deque
n,m = map(int,input().split()) # 정점의 개수,간선의 개수

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for i in range(n+1)]

# 탐색 시작은 1에서 시작
def bfs():
    # 시작정점 방문처리
    visited[1] = 0
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == -1: # 한번도 방문하지 않은 정점이라면
                visited[i] = visited[node] + 1 # 거리 누적 기록
                queue.append(i)

bfs()

# 가장 긴 길이 계산
max_length = max(visited)

result = [] # 정답 인덱스를 저장할 배열

for i in range(len(visited)):
    if visited[i] == max_length:
        result.append(i)

print(result[0],max_length,len(result))
