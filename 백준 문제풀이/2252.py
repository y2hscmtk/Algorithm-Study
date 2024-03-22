# https://www.acmicpc.net/problem/2252
'''
N명의 학생을 키 순서대로 줄 세우기
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 
이는 "학생 A가 학생 B의 앞에 서야 한다는 의미이다." => 위상 정렬
학생들의 번호는 1번부터 N번이다.
답이 여러 가지인 경우에는 아무거나 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
'''
위상 정렬 알고리즘
1. 진입차수가 0인 정점을 큐에 삽입한다.
2. 큐에서 정점을 팝하여 방문하고, 해당 정점과 연결된 다른 정점에 대한 간선을 제거한다.(진입차수-1)
3. 위 결과로 진입차수가 0이 된 정점을 다시 큐에 삽입한다.
모든 정점을 방문할 때 까지 1~3 과정을 반복한다.
'''
indegree = [0]*(N+1) # 방문 정보
indegree[0] = -1 # 인덱스 0인 학생은 없음
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    indegree[b] += 1 # b를 방문하기 전에 먼저 방문해야 하는 정점이 존재한다.
    graph[a].append(b) # 간선정보 삽입
# 1. 진입차수가 0인 정점 모두 큐에 삽입한다.
queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i) # 해당 인덱스 삽입

# 2. 큐에서 정점을 팝하여 방문하고, 연결된 다른 정점에 대한 간선을 제거한다.(진입차수-1)
while queue:
    current = queue.popleft() # 진입 차수가 0인 정점 뽑기
    print(current,end=' ') # 방문 처리
    # 해당 정점과 연결된 모든 간선 제거
    for node in graph[current]:
        indegree[node] -= 1
        if indegree[node] == 0: # 그 결과로 인해 진입차수가 0이 되었다면
            queue.append(node) # 정점 삽입