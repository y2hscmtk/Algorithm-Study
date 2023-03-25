# https://www.acmicpc.net/problem/18352
'''
도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
'''
from collections import deque
# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
n, m, k, x = map(int, input().split())

# 정점의 개수(n), 간선의 개수(m), 간선 경로k, 탐색 시작 정점 x

# 도시의 개수n개 만큼 빈 배열 생성
# 0번 도시는 존재하지 않으므로 n+1개 생성
graph = [[] for _ in range(n+1)]

visited = [-1 for _ in range(n+1)]
visited[x] = 0  # 시작 정점은 방문처리

# 시작 정점은 x
# bfs수행


def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        curr_node = queue.popleft()
        # 인접 정점 방문
        for node in graph[curr_node]:
            # 아직 방문하지 않았다면 방문하고 큐에 삽입
            if visited[node] == -1:
                visited[node] = visited[curr_node] + 1  # 경로 +1 처리
                queue.append(node)


# A, B => a번 도시에서 b번도시로의 경로가 존재함을 의미
for _ in range(m):
    a, b = map(int, input().split())
    # 간선 정보 입력
    graph[a].append(b)

bfs(x)

result = []

for i in range(1, n+1):
    # 정확히 k에 해당한다면
    if visited[i] == k:
        result.append(i)

if len(result) != 0:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
