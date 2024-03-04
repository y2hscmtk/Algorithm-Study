# https://www.acmicpc.net/problem/1922
'''
정점 N (1<=N<=1000)
간선 M (1<=M<=100,000)
정점의 개수가 적고, 간선의 개수가 많으므로 프림 알고리즘 선택
'''
import heapq,sys
input = sys.stdin.readline
n = int(input())
v = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a,b,cost = map(int,input().split())
    v[a].append((b,cost))
    v[b].append((a,cost))
queue = [(0,1)] # 최소힙 cost,next
visited = [False]*(n+1)
# 현재 집합에 포함되어있는 노드들의 간선을 최소힙에 삽입
result = 0
while queue:
    cost,next = heapq.heappop(queue) # 가격이 최소인 간선 팝하기
    # 다음에 가려는 장소가 이미 집합에 포함되어있다면 다른 값으로
    if visited[next]:
        continue
    visited[next] = True # 아직 방문하지 않았다면 방문처리
    result += cost # 간선을 선택하였으므로 +cost
    # next와 연결된 간선들도 최소 힙에 삽입
    for node,value in v[next]:
        heapq.heappush(queue,(value,node))
print(result)