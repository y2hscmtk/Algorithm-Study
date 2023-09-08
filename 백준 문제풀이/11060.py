# https://www.acmicpc.net/problem/11060
'''
재환이는 Ai이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다. 
예를 들어, 3번째 칸에 쓰여 있는 수가 3이면, 재환이는 4, 5, 6번 칸 중 하나로 점프할 수 있다.
'''
from collections import deque
n = int(input())
data = list(map(int, input().split()))


def bfs():
    visited = [0]*n  # 최단 횟수를 기록하기 위함
    queue = deque()
    queue.append(0)  # 시작 인덱스 삽입
    while queue:
        now = queue.popleft()  # 현재 인덱스
        # 목적지에 도달하였는지 확인
        if now == n-1:
            return visited[now]
        if data[now] == 0:  # 0이라면 점프 불가능
            continue
        for x in range(1, data[now]+1):
            nx = now + x  # 다음에 이동할 칸 선정
            # 영역을 벗어나지 않는지 확인
            # 아직 방문하지 않은 경우에 한해서
            if nx < n and visited[nx] == 0:
                visited[nx] = visited[now] + 1  # 점프 횟수 추가
                queue.append(nx)  # 큐에 삽입
    return -1  # 목적지에 도달하지 못할 경우


print(bfs())
