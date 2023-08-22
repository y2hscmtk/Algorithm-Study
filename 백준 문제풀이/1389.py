# https://www.acmicpc.net/problem/1389
'''
모든 사람에 대해서 가중치를 1로 두고 최단거리 탐색 진행
다른 사람을 통해서 더 빨리 만날수 있다면 가중치값이 줄어든 것으로 판단하여 갱신
케빈 베이킨의 수가 가장 작은 사람 = 가중치의 합이 가장 작은 사람
'''
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):  # 관계 입력받기
    A, B = map(int, input().split())
    # A와 B는 친구다
    graph[A].append(B)
    graph[B].append(A)


# 다익스트라 수행 => 각 정점별 가중치는 1임
def dijkstera(start):
    distance = [INF]*(N+1)  # 각 사람을 만나기 까지 걸린 시간
    distance[start] = 0  # 시작 지점으로의 가중치는 0
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        # 해당 사람의 모든 친구관계 조사
        for p in graph[node]:
            # 만약 해당 사람을 통해 p사람을 만나는게
            # 기존에 p를 만났던거보다 더 빨리 만나는 일이라면
            if distance[node] + 1 < distance[p]:
                distance[p] = distance[node] + 1  # 시간 갱신
                queue.append(p)
    # 다익스트라 알고리즘 수행 이후
    # INF가 아니라면 케빈케이컨 계산에 포함하여 리턴
    kvc = 0  # 케빈케이컨
    for time in distance:
        if time == INF:
            continue
        kvc += time
    return kvc  # start사람의 케빈 베이컨 수 리턴


kavin = INF
# 모든 사람들이 한번씩 다익스트라 수행
for i in range(1, N+1):
    temp = dijkstera(i)
    if temp < kavin:  # 작은 경우에만 갱신
        kavin = temp
        result = i
print(result)
