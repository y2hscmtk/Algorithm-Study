# https://www.acmicpc.net/problem/24483
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [-1]*(n+1) # 방문 정보
graph = [[] for _ in range(n+1)] # 간선정보 기록
count,result = 0,0 # 방문순서, 정답
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 간선 그래프 방문 순서는 오름차순
for g in graph:
    g.sort()

# dfs
def dfs(r,depth):
    global count,result
    count+=1
    visited[r] = count*depth
    result += visited[r]
    for node in graph[r]:
        if visited[node] == -1:
            dfs(node,depth+1)
    

dfs(r,0) # dfs 수행
print(result)