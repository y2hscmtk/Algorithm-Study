# https://www.acmicpc.net/problem/15971
'''
두 정점 사이의 최단 경로를 기록하고 => 다익스트라 => bfs
가장 긴 거리를 제외한 나머지 거리를 더해서 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

N, start, end = map(int, input().split())

graph = [[] for _ in range(N+1)]  # 1번 방부터 N번 방까지

for _ in range(N-1):
    # a에서 b까지 가는 거리는 c(양 방향)
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs():
    queue = deque()
    queue.append([start, 0, 0])
    visited = [-1]*(N+1)
    visited[start] = 0  # 시작 좌표까지의 거리는 0
    while queue:
        curr_node, curr_d, max_length = queue.popleft()
        if curr_node == end:  # 목적지 도달시
            print(visited[end]-max_length)
        for node, dist in graph[curr_node]:
            if visited[node] == -1:
                visited[node] = curr_d + dist
                max_length = max(max_length, dist)
                queue.append([node, visited[node], max_length])


bfs()
