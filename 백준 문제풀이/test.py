# https://www.acmicpc.net/problem/13549
'''
출발지 n과 목적지 k가 주어졌을때 k에 도달하는데 걸리는 시간을 측정
n에서 n-1과 n+1로 이동하는데는 각각 1초가 걸리지만
2*n으로 이동하는데는 0초의 시간이 걸린다
=> 아이디어 오류 폐기, 그냥 bfs로 수정
'''
from collections import deque

n,k = map(int,input().split())

# 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다 => 최대 배열의 크기 설정
graph = [-1 for _ in range(100001)]
visited = [False for _ in range(100001)]

queue = deque()
# 모든 순간이동 좌표 방문처리후 큐에 삽입
for nx in range(n,100001,+n):
    # 범위를 벗어나지 않는 선에서
    if 0<=nx<100001:
        graph[nx] = 0
        queue.append(nx)
        visited[nx] = True
    else:
        break

# 시작위치 n은 방문처리하고 목적지 k에 도달할때까지 bfs를 수행한다
def bfs():
    global queue
    visited[n] = True
    graph[n] = 0
    while queue:
        x = queue.popleft()
        # 목적지에 도달하였다면 종료
        if x==k:
            return graph[x]
        # 좌우로 이동하는 경우만 생각
        for nx in (x + 1, x - 1):
            # 범위를 벗어나지 않으면서 방문하지 않은 점에 대하여
            if 0<=nx<100001 and not visited[nx]:
                graph[nx] = graph[x] + 1 # 1초를 누적시키고
                queue.append(nx) # 큐에 삽입
                visited[nx] = True # 방문처리 후
print(bfs())