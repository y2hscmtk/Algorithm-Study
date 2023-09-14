# https://www.acmicpc.net/problem/24479

'''
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 
간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 '양방향 간선'을 나타낸다. 
(1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 '오름차순'으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)] # 정점에 대한 간선 정보를 담기 위한 배열
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 정보를 담고 있음
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1) # 모든 노드에 대한 방문정보를 저장하기 위한 방문 배열

# 오름차순으로 방문을 하는 dfs함수 정의
def dfs(start): # 탐색을 시작하는 노드
    global cnt
    visited[start] = cnt # 방문처리
    graph[start].sort() # 오름차순으로 방문해야하므로 정렬
    for node in graph[start]: # 현재 노드에 연결된 모든 간선 정보 오름차순으로 분석
        if visited[node]==0: # 아직 방문하지 않았다면
            cnt+=1
            dfs(node) # 인접 노드를 기준으로 다음 노드로 방문처리

cnt = 0
dfs(r) # 시작노드에서 탐색 시작

# 시작노드에서 방문할수 없다면 0을 출력한다.
# 방문한 순서대로 정답을 출력해야 한다.
for i in range(1,len(visited)):
    print(visited[i])
    