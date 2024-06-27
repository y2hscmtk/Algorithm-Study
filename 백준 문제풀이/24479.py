# https://www.acmicpc.net/problem/24479
'''
시작 정점은 R, 인접정점은 오름차순으로 방문한다.
각 줄에 방문 순서를 하나씩 출력한다.
방문하지 못하였으면 0을 출력한다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 0 # 시작 순서는 1부터
def dfs(node):
    global visited,count
    # 현재 노드 방문 처리
    count+=1
    visited[node] = count
    # 인접노드 오름차순 정렬
    graph[node].sort()
    for n in graph[node]: # 인접 노드들 중에서
        if visited[n] == 0: # 아직 방문하지 않은 인접노드에 대해서
            dfs(n) # 깊이우선탐색 수행
# 간선 정보 입력받기
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)    

# 깊이우선 탐색 수행
dfs(R)
for i in range(1,len(visited)):
    print(visited[i])
    