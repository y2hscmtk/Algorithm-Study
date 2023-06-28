# https://www.acmicpc.net/problem/13549
'''
출발지 n과 목적지 k가 주어졌을때 k에 도달하는데 걸리는 시간을 측정
n에서 n-1과 n+1로 이동하는데는 각각 1초가 걸리지만
2*n으로 이동하는데는 0초의 시간이 걸린다
'''
from collections import deque

n,k = map(int,input().split())

# 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다 => 최대 배열의 크기 설정
graph = [-1 for _ in range(100001)]

dx = [2,-1,1]

# 시작위치 n은 방문처리하고 목적지 k에 도달할때까지 bfs를 수행한다
def bfs():
    queue = deque()
    queue.append(n)
    graph[n] = 0
    while queue:
        x = queue.popleft()
        # 목적지에 도달하였다면 종료
        if x==k:
            return graph[x]
        # 좌우로 이동하는 경우만 생각
        for i in range(3):
            if i==0: # 순간이동의 경우
                nx = x * dx[i]
                if 0 <= nx <= 100001 and graph[nx]==-1:
                    queue.append(nx) 
                    graph[nx] = graph[x] # 순간이동은 시간소요x
            else:
                nx = x + dx[i]
                if 0<=nx<100001 and graph[nx]==-1:
                    queue.append(nx)
                    graph[nx] = graph[x] + 1 # 걸어가는 경우 1초 소요        
print(bfs())
