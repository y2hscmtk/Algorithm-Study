# https://www.acmicpc.net/problem/25418
'''
입력으로 양의 정수 A와 K가 주어지면, 아래 연산을 이용하여 A를 K로 변경하려고 한다. 정수 A를 변경할 때 사용할 수 있는 연산 종류는 다음과 같다.

연산 1: 정수 A에 1을 더한다.
연산 2: 정수 A에 2를 곱한다.
정수 A를 정수 K로 만들기 위해 필요한 최소 연산 횟수를 출력하자.
'''
import sys
input = sys.stdin.readline
from collections import deque
# 1 ≤ A < K ≤ 1,000,000
A, K = map(int,input().split())
visited = [-1 for _ in range(K+1)]
# 정수 A를 K로 만들기
def bfs():
    queue = deque()
    queue.append(A)
    visited[A] = 0 # 시작좌표 방문처리
    while queue:
        x = queue.popleft()
        # K 도달시 종료
        if x == K:
            return visited[x]
        # 1을 더하거나 2를 곱하거나
        for nx in [x+1,x*2]:
            if 0<=nx<=K and visited[nx] == -1:
                visited[nx] = visited[x] + 1 # 방문처리, 최소 횟수 업데이트
                queue.append(nx)

print(bfs())