# https://www.acmicpc.net/problem/12761
'''
돌의 번호는 0부터 100,000까지 존재, 동규는 N번째 돌 위에, 주미는 M번 돌 위에 위치하고 있다.
동규는 좌우로 +1,-1 이동 가능, A나 B만큼 좌우로 점프 할 수 있음, 현 위치에서 A배나 B배의 위치로 이동할 수 있음
'''
from collections import deque
A,B,N,M = map(int,input().split())
visited = [0 for _ in range(100001)] # 방문정보 확인용

# N번에서 M으로 최단 거리로 이동할 수 있는 방법
def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x = queue.popleft()
        # 목적지에 도달하였다면 최소 횟수 리턴
        if x == M:
            return visited[x]
        # 좌우로 이동하는 경우, A만큼 점프 하는 경우, B만큼 점프하는 경우, A배 이동하는 경우, B배 이동하는 경우
        for nx in [x+1,x-1,x+A,x-A,x+B,x-B,x*A,x*B]:
            # 이동 과정에서 100000보다 크거나 0보다 작은 번호의 돌로는 이동할 수 없다.
            if 0<=nx<=100000 and visited[nx] == 0: # 방문한적 없는 영역만 방문 가능
                visited[nx] = visited[x] + 1 # 이동횟수 추가
                queue.append(nx)
    # 항상 도달할 수 있는 케이스만 주어진다.

print(bfs(N))