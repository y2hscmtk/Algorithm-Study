# https://www.acmicpc.net/problem/11403

'''
문제
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. 
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
'''
import sys
from collections import deque
input = sys.stdin.readline


# bfs 정의
def bfs(start):
    global graph, result
    queue = deque([start])
    # start 노드에 대하여 bfs를 수행,
    # j번 노드에 방문이 가능하다면 => result[start][j] = 1
    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:  # 해당 정점의 인접 정점 탐색
            if result[start][adj_node] == 0:  # 아직 방문한적 없다면
                result[start][adj_node] = 1  # 방문처리
                queue.append(adj_node)  # 인접정점 큐에 삽입


# 정점의 개수
n = int(input())

# 인접정보를 저장할 그래프 생성
graph = [[] for i in range(n)]

# 인접정보 입력받기, 자기번호에 해당하는 값은 항상 0
for i in range(n):
    adj_list = list(map(int, input().split()))
    for j in range(n):
        if adj_list[j] == 1:  # 1은 i에서 j로의 경로가 있음을 의미
            graph[i].append(j)

# 경로가 있는지 여부를 저장할 배열 => 모두 0으로 초기화하여 생성
result = [[0]*n for i in range(n)]

# 모든 정점에 대하여 bfs
for i in range(n):
    bfs(i)

# 정답 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print("")
