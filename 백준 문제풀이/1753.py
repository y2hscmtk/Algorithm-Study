# https://www.acmicpc.net/problem/1753

'''
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 

단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
(1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. 
u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
'''
'''
아이디어1 : 다익스트라 알고리즘으로 풀어보자
'''
# 다익스트라 알고리즘 : 한 정점에서 다른 정점까지의 최단 경로를 구하는 알고리즘
# 최단경로가 발견된 정점을 기록할 배열 found 배열, 최단경로의 길이를 저장할 배열 distance배열이 필요
# distance[i][j]는 정점 i에서 정점 j까지의 거리를 기록 => 길이 없다면 INF를 저장(무한)

# 해당문제는 단방향 그래프임에 유의

import sys
import heapq # 시간초과판정을 피하기 위해 최소힙사용
v, e = map(int, input().split())  # v정점의 개수,e간선의 개수
k = int(input())  # 탐색을 시작할 정점

INF = sys.maxsize  # 무한을 표현하기 위해

graph = [[] for _ in range(v+1)]  # 그래프 간선 저장용

# 최단경로를 저장할 배열, 탐색 시작정점에서 정점u까지의 최단경로를 distance[u]로 표현한다.
distance = [INF]*(v+1)

for _ in range(e):
    # i에서j로 가는 길의 가중치 w
    i, j, w = map(int, input().split())
    graph[i].append([w, j])  # u에서 v로의 경로와 가중치를 저장

# 다익스트라 알고리즘
distance[k] = 0  # 시작 정점의 거리 0으로 초기화
heap = []  # 최소힙으로 사용
heapq.heappush(heap, [0, k])  # 가중치0, 시작정점 k을 heap에 heappush함

while heap:
    # heap에서 가중치가 가장 작은 노드를 pop(heappop)
    weight, node = heapq.heappop(heap)

    # # 기존 경로가 더 짧다면 distance업데이트x
    # if distance[node] < weight:
    #     continue

    # node를 통해서 갈때 더 짧다면 distance배열 업데이트
    for w, n in graph[node]:
        if w+weight < distance[n]:  # k에서 n으로의 거리를 더 단축시킬수 있다면
            distance[n] = w + weight  # 값 업데이트
            # 최소힙에 삽입
            heapq.heappush(heap, [w+weight, n])

# 결과 출력
for i in range(1, v+1):
    # 경로가 없다면 INF 출력
    print("INF" if distance[i] == INF else distance[i])
