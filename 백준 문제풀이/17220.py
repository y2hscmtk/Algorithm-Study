# https://www.acmicpc.net/problem/17220
from collections import deque
N, M = map(int, input().split())
graph = {}
for i in range(N):
    graph[chr(65 + i)] = []

# 마약 공급책 간의 관계 입력 받기
edges = []
for _ in range(M):
    s, e = input().split()
    graph[s].append(e)
    edges.append((s, e))

# 경찰이 파악 중인 마약 공급책들 입력 받기
input_line = input().split()
targets = set(input_line[1:])  # 검거된 공급책들

# 원래 그래프에서 진입 차수 계산 => 진입차수가 0인 경우 -> 원산지
in_degree = {node: 0 for node in graph}
for s, e in edges:
    in_degree[e] += 1

# 마약의 원산지 찾기 (검거된 공급책 제외)
origins = [node for node in graph if in_degree[node] == 0 and node not in targets]

# 그래프에서 검거된 공급책 및 간선 제거
for t in targets:
    if t in graph:
        del graph[t]

for node in graph:
    graph[node] = [neighbor for neighbor in graph[node] if neighbor not in targets]

visited = set()
def bfs(start_nodes):
    queue = deque(start_nodes)
    visited.update(start_nodes)
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(origins)

# 마약 원산지를 제외한 공급처 출력
print(len(visited) - len(origins))
