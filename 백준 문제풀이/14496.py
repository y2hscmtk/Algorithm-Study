# https://www.acmicpc.net/problem/14496
from collections import deque

a, b = map(int,input().split())
# 둘째 줄에 전체 문자의 수 N과 치환 가능한 문자쌍의 수 M이 주어진다
n, m = map(int,input().split())
# a -> b, n개의 문자, m개의 쌍
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start,end = map(int,input().split())
    # 그래프는 단 방향
    graph[start].append(end) # 갈 수 있는 경로 기록
    graph[end].append(start)

def bfs():
    visited = [-1]*(n+1)
    visited[a] = 0 # 시작 노드는 0 처리
    queue = deque()
    queue.append(a)
    while queue:
        node = queue.popleft()
        if node == b:
            return visited[b]
        for next_node in graph[node]:
            # 아직 방문하지 않은 노드에 한해서
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1 # 방문처리
                queue.append(next_node)
    return -1 # 탐색 불가인 경우

print(bfs())
