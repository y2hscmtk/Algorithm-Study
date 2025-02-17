'''
모든 리프 노드에 말이 하나씩 존재
존재하는 말 중 하나를 골라, 부모 노드로 옮긴다
한 노드에 여러개의 말이 존재할 수 있음
루트 노드에 말이 도착하면 말 제거
루트 노드는 1번
더 이상 옮길 말이 없는 상태에서 차례가 돌아온 사람의 패배
A가 승리할 수 있는지 판단하는 프로그램 작성

루트노드에서 모든 리프노드까지의 거리의 합이 
짝수라면 B의 승리,
홀수라면 A의 승리가 될 것
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs():
    queue = deque([(1, 0)])  # (현재 노드, 깊이)
    visited = [False] * (N+1)
    visited[1] = True
    total_depth = 0  # 리프 노드까지의 거리 총합

    while queue:
        node, depth = queue.popleft()
        is_leaf = True

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, depth + 1))
                is_leaf = False  # 자식이 있는 노드는 리프가 아님

        if is_leaf:  # 리프 노드일 때 깊이를 더함
            total_depth += depth

    return total_depth

length = bfs()

# 거리의 합이 홀수이면 A 승리(1), 짝수이면 B 승리(0)
print(1 if length % 2 == 1 else 0)