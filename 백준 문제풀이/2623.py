# https://www.acmicpc.net/problem/2623
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = [] # 최종 순서를 저장하기 위한 배열
for _ in range(M):
    order = list(map(int,input().split()))
    # 연결 정보 만들기
    for i in range(1,len(order)-1):
        a,b = order[i],order[i+1]
        graph[a].append(b) # 연결 정보 표시
        indegree[b] += 1 # 진입차수 증가
        
# 진입차수가 0인 정점을 큐에 삽입
queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft() # 진입차수가 0인 정점 팝
    result.append(current)
    # 현재 진입차수와 관련된 모든 간선 제거(진입차수 -1)
    for node in graph[current]:
        indegree[node] -= 1
        if indegree[node] == 0: # 그로인해 진입차수가 0이 되었다면
            queue.append(node) # 정점 삽입

# 만약 남훈이가 순서를 정하는게 불가능 하다면, 첫째 줄에 0을 출력한다.
# 순서를 정할 수 없는 경우 -> 모든 정점을 방문할 수 없는 경우
if len(result) != N:
    print(0)
else: # 순서를 정할 수 있다면 숫자 한 개 씩 출력
    for r in result:
        print(r)