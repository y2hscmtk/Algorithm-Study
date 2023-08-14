# https://www.acmicpc.net/problem/14938
'''
모든 노드를 돌면서, 해당 노드에 대해서 최단거리 리스트를 생성
최단거리 리스트 생성 이후, 수색범위를 넘어서지 않는 다면 아이템 수를 누적시켜 더한다.
각 노드에 대해 탐색이 끝나면 최대 아이템 수를 갱신한다.
'''
import sys
import heapq
input = sys.stdin.readline

# 노드의 개수, 수색 범위, 간선의 개수
n, m, r = map(int, input().split())
# 각 노드별 아이템의 수
item = list(map(int, input().split()))
# 노드 그래프 생성
graph = [[] for _ in range(n+1)]  # 1번 노드부터 시작되므로
# 간선 정보 입력받기
for _ in range(r):
    a, b, l = map(int, input().split())
    # a에서 b까지 가는데, 거리 l이 걸린다.
    graph[a].append([l, b])
    graph[b].append([l, a])


# 해당 노드를 기준으로 각 노드까지의 최단거리 계산
def dijkstera(node):
    global distance, q
    q = []  # 최소힙으로 사용할 배열
    heapq.heappush(q, (0, node))  # 자기 자신은 거리 0
    distance[node] = 0  # 자기 자신은 거리 0
    # 착륙한 노드에서 각 노드별 최단거리 갱신
    while q:
        curr_d, i = heapq.heappop(q)
        # 인접한 노드들 최단거리 갱신
        for d, next_node in graph[i]:
            # 거리가 갱신 된다면(더 짧아진다면)
            if curr_d + d < distance[next_node]:
                distance[next_node] = curr_d + d  # 최단 거리 갱신
                heapq.heappush(q, (distance[next_node], next_node))


INF = int(1e9)
result = -1
# 어떤 노드에 착륙할지 결정
for node in range(1, n+1):
    # 해당 노드에서 각 노드까지의 최단거리 계산
    distance = [INF]*(n+1)
    # 다익스트라 수행
    dijkstera(node)
    # 수행 이후, 수색범위에 드는 노드들 방문하면서 아이템 더하기
    temp = 0
    for i, d in enumerate(distance):
        if d <= m:  # 수색범위에 들어오는 거리라면
            temp += item[i-1]
    result = max(result, temp)  # 최대값 갱신

print(result)
