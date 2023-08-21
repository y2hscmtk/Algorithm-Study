# https://www.acmicpc.net/problem/1916
import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # a에서 b를 가는데 비용 c가 든다.


def dijkstera(start):
    INF = int(1e9)
    distance = [INF]*(N+1)
    queue = []
    heapq.heappush(queue, (0, start))  # 최소힙에 자기자신으로의 비용을 0으로 두고 start 삽입
    while queue:
        # 현재 정점에서 갈 수 있는 가장 최단 거리의 노드와 비용
        curr_cost, curr_node = heapq.heappop(queue)
        # 더이상 고려할 필요가 없다면
        if distance[curr_node] < curr_cost:
            continue

        # 만약 거리가 갱신된다면 업데이트 후 큐에 삽입
        for cost, node in graph[curr_node]:
            # 현재 정점까지의 거리 + node까지의 거리 < 시작 정점에서 바로 node로 가는 거리
            if curr_cost + cost < distance[node]:
                distance[node] = curr_cost + cost  # 거리 갱신
                heapq.heappush(queue, (distance[node], node))

    return distance[end]


start, end = map(int, input().split())
print(dijkstera(start))
