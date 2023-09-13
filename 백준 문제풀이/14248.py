# https://www.acmicpc.net/problem/14248
from collections import deque
n = int(input())
data = list(map(int,input().split()))
start = int(input())

def bfs(start):
    queue = deque()
    queue.append(start-1) # 탐색을 시작할 노드 설정
    visited = [False]*(n)
    visited[start-1] = True # 탐색 시작좌표 방문처리
    # 각 칸에 적혀있는 숫자만큼 좌우로 이동할수 있음
    while queue:
        node = queue.popleft()
        for nx in (node+data[node],node-data[node]):
            # 영역을 벗어나지 않으면서
            # 방문하지 않은 nx라면 방문처리후 큐에 삽입
            if 0<=nx<n and not visited[nx]:
                visited[nx] = True # 방문처리
                queue.append(nx)
            
    # 방문가능한 칸의 개수 리턴
    return visited.count(True)

print(bfs(start))