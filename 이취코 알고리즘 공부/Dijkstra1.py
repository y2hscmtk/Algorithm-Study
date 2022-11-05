# 다익스트라 알고리즘

# 최단경로 문제

# 각 지점을 그래프의 노드로 표현, 지점 간 연결된 도로는 간선으로 표현한다.

# 다익스트라 알고리즘: 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산하는 알고리즘
# 음의 간선이 없는 상황에서 사용하며, 매 순간 최선의 선택을 지양하기 때문에 그리디 알고리즘의 기법과 유사하다.


# 1. 출발 노드 설정
# 2. 최단 거리 테입르 초기화
# 3. 방문하지 않은 노드 중, 최단 거리가 가장 짧은 노드를 선택
# 4. 해당노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 5. 위 과정에서 3번과 4번을 반복한다.

from asyncio.windows_events import INFINITE
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[]for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화 => 다이나믹 프로그래밍
distance = [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c, = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))  # 튜플 형태로 입력

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]  # 해당 노드까지의 거리 갱신
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
