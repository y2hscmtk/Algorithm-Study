# https://www.acmicpc.net/problem/24482
'''
N개의 정점과 M개의 간선으로 이루어진 무방향 그래프, 정점 번호는 1번부터 N번 모든 간선의 가중치는 1
정점 R에서 dfs 수행, 탐색 수행 과정 중의 모든 노드의 깊이(depth) 출력, 방문되지 않은 노드의 깊이는 -1로 출력
인접 정점은 내림차순으로 방문
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
N,M,R = map(int,input().split())
visited = [-1 for _ in range(N+1)] # 정점 번호는 1번 부터 시작
graph = [[] for _ in range(N+1)]

def dfs(node,depth):
    # 인접 정점들을 기준으로(내림차순) 방문
    for n in sorted(graph[node],reverse=True):
        if visited[n] == -1: # 아직 방문하지 않았다면
            visited[n] = depth # 깊이 저장
            dfs(n,depth+1) # 다음 노드 방문 시작

for _ in range(M):
    s,e = map(int,input().split())
    # 간선 정보 입력
    graph[s].append(e)
    graph[e].append(s)

# 정점 R에서 탐색 시작
visited[R] = 0 # 시작 노드는 깊이 0번
dfs(R,1)

for i in range(1,N+1):
    print(visited[i])
