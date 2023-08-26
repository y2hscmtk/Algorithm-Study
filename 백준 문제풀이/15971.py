# https://www.acmicpc.net/problem/15971
'''
두 정점 사이의 최단 경로를 기록하고 => 다익스트라
가장 긴 거리를 제외한 나머지 거리를 더해서 출력
'''
import heapq
import sys
input = sys.stdin.readline

N, start, end = map(int, input().split())

graph = [[] for _ in range(N+1)]  # 1번 방부터 N번 방까지

for _ in range(N-1):
    # a에서 b까지 가는 거리는 c(양 방향)
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra():
    INF = int(1e9)
    queue = []
    distance = [[INF, -1] for _ in range(N+1)]
    # distance배열 값 초기화
    for node, dist in graph[start]:
        distance[node][0] = dist
        distance[node][1] = dist
        heapq.heappush(queue, (dist, node))
    distance[start][0] = 0  # 자기 자신으로의 최단거리는 0
    while queue:
        curr_d, curr_node = heapq.heappop(queue)
        for node, dist in graph[curr_node]:
            # curr_node를 거쳐갈 경우,
            # node로의 최단거리가 갱신된다면 거쳐가기
            # curr_d는 curr_node까지의 최단거리
            if curr_d+dist < distance[node][0]:
                distance[node][0] = curr_d+dist
                distance[node][1] = max(distance[node][1], dist)
                heapq.heappush(queue, (distance[node][0], node))
    return distance


distance = dijkstra()
print(distance[end][0] - distance[end][1])
