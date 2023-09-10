# https://www.acmicpc.net/problem/5567
'''
1에서부터 각 노드까지의 거리 계산
계산이후 거리가 1(친구) 또는 2(친구의 친구)인 값의 수 출력
'''
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
visited = [-1]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)  # 친구관계 추가
    graph[b].append(a)


def bfs():
    global visited
    queue = deque()
    queue.append(1)  # 1번에서부터 탐색 시작
    visited[1] = 0  # 자기 자신
    while queue:
        me = queue.popleft()
        for friend in graph[me]:
            if visited[friend] == -1:  # 아직 관계파악 안된 친구
                visited[friend] = visited[me] + 1
                queue.append(friend)


bfs()
result = visited.count(1) + visited.count(2)
print(result)
