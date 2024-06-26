# https://www.acmicpc.net/problem/24445
'''
무방향 그래프(undirected graph)가 주어진다
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000),
간선의 수 M (1 ≤ M ≤ 200,000), 
시작 정점 R (1 ≤ R ≤ N)이 주어진다.
시작정점은 1이다. 인접 정점은 내림차순으로 방문한다.
각 정점의 방문 순서를 차례로 출력한다. => visited 배열 출력
시작정점에서 방문할 수 없는 경우 0을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
# 인접정점의 경우 내림차순으로 방문한다.
def bfs():
    global visited
    turn = 1 # 방문순서
    queue = deque()
    queue.append(R) # 방문정점은 R
    visited[R] = 1 # 1번 노드는 시작하자마자 방문
    while queue:
        x = queue.popleft() # 시작 노드 팝
        # 인접 노드 내림차순 정렬 후 방문
        t = sorted(graph[x],reverse=True)
        for i in t: # 인접 정점에 대해서
            if visited[i] == 0: # 방문하지 않은 정점에 대해서만 방문
                turn += 1
                visited[i] = turn # 방문처리
                queue.append(i) # 해당 정점 큐에 삽입

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)] # 인접정점 그래프
visited = [0]*(N+1) # 방문순서
# 간선 정보
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs()
# 한줄에 한 개 씩 방문 정보를 출력한다.
for i in range(1,len(visited)):
    print(visited[i])