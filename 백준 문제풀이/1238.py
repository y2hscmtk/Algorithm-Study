# https://www.acmicpc.net/problem/1238
'''
한 마을에서 출발하여 X번 마을에 도착한 후, 다시 되돌아 오는데 걸리는 시간 계산
그 시간들 중 가장 오래 걸린 시간 출력
각 마을에서 X번 마을까지의 최단 거리를 구한후, X번 마을에서 각 마을까지의 최단 거리를 더하면 될듯
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 집은 1번부터 시작
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([t, b])  # a에서 b로 가는데 t만큼의 시간이 걸린다.


# 최단 거리 계산
def dijkstera(node):
    global distance
    # 시작 노드에서 갈 수 있는 모든 경로 파악
    queue = []  # 최소 힙으로 사용할 배열
    for cost, next_node in graph[node]:  # 시작 정점에서 갈 수 있는 모든 경로 업데이트
        distance[next_node] = cost  # next_node로 가는데 cost만큼의 비용 소모
        heapq.heappush(queue, (cost, next_node))  # 비용을 우선으로 최소힙에 삽입

    while queue:
        # 현재 노드에서 가장 비용이 적게 드는 노드 팝
        curr_cost, curr_node = heapq.heappop(queue)
        for cost, next_node in graph[curr_node]:
            # 비용이 갱신된다면 최소힙에 삽입
            # 현재노드까지의 비용 + 현재 노드에서 next_node로의 비용 < 시작노드에서 next_node로의 비용
            if curr_cost+cost < distance[next_node]:
                distance[next_node] = curr_cost+cost  # 비용 갱신
                heapq.heappush(queue, (distance[next_node], next_node))


result = [0]*(N+1)
for i in range(1, N+1):
    # 각 마을에서 X번째 마을로 가는데 걸리는 최단거리 기록
    distance = [INF] * (N+1)  # i번째 마을에서 X번째 마을로의 최단 거리 : distance[i]
    # X인경우는 무시
    if i == X:
        continue
    dijkstera(i)
    result[i] = distance[X]  # X까지의 최단거리를 기록

distance = [INF] * (N+1)  # i번째 마을에서 X번째 마을로의 최단 거리 : distance[i]
dijkstera(X)  # X에서 각 마을까지의 최단거리 계산
for i in range(1, N+1):
    result[i] += distance[i]  # 각 마을까지의 최단 거리 더하기(되돌아가기)

# 가장 오래걸리는 시간 정답으로 출력
print(max(result))
