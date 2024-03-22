# https://www.acmicpc.net/problem/1766
'''
<위상정렬>
1. 진입차수가 0인 정점 큐에 삽입
2. 큐에서 뽑아서 방문 처리 후, 연결된 모든 간선들 진입차수 -1(연결된 간선 제거)
3. 간선을 제거한 후 진입 차수가 0이 된 정점을 큐에 삽입
4. 모든 정점을 방문할 때 까지 1~3 반복
'''
import sys,heapq # 우선순위 큐 활용
input = sys.stdin.readline
N,M = map(int,input().split()) # 문제의 수(정점의 수), 정보의 수
indegree = [0]*(N+1) # 진입 차수 => 해당 노드로의 진입차수가 몇개인지 파악
indegree[0] = -1 # 0번째 문제는 존재하지 않으므로
graph = [[] for _ in range(N+1)] # 연결 정보
for _ in range(M):
    a,b = map(int,input().split()) # b를 풀기 전에 a를 먼저 풀어보는 것이 좋다.
    graph[a].append(b) # a에서 진입 가능한 정점으로 b삽입
    indegree[b]+=1 # b를 가리키고 있는 노드가 한 개 존재
'''
1. N개의 문제는 모두 풀어야 한다.
2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
3. 가능하면 쉬운 문제부터 풀어야 한다. (번호가 낮은 순서대로)
'''
# 먼저 진입차수가 0인 정점들을 큐에 삽입한다.
queue = [] # 최소 힙으로 사용할 배열
for i in range(1,N+1):
    if indegree[i] == 0: # 진입차수가 0이라면
        heapq.heappush(queue,i) # 진입차수가 0인 노드 숫자 작은 순서대로 삽입(쉬운 문제 먼저 풀어야함)

# 모든 정점을 방문할 때 까지 반복
while queue:
    # 진입차수가 0인 정점 팝
    current = heapq.heappop(queue)
    print(current,end=' ') # 방문 정점 출력 
    # 해당 정점과 연결 되어 있는 간선 제거
    for node in graph[current]:
        indegree[node] -= 1 # 간선 제거(진입 차수 -1)
        if indegree[node] == 0: # 진입 차수 제거로 인해 차수가 0이 되었다면
            heapq.heappush(queue,node) # 정점 삽입
