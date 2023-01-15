# https://www.acmicpc.net/problem/11725

'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
'''

from collections import deque
# BFS에 이용할 큐
queue = deque()

n = int(input())

# 리스트를 이용하여 트리 구현
tree = [[] for i in range(n+1)]

for i in range(n-1):
    # 인접관계 입력받기
    nodes = list(map(int, input().split()))
    tree[nodes[0]].append(nodes[1])
    tree[nodes[1]].append(nodes[0])

# 부모 노드를 저장할 배열
parent = [0 for i in range(n+1)]


# BFS를 통해 부모노드 배열을 갱신한다.
def BFS():
    queue.append(1)
    # 큐가 비어있지 않은 동안 탐색
    while queue:
        root = queue.popleft()
        # 방문하지 않은 노드만 방문
        for nodes in tree[root]:
            if parent[nodes] == 0 and nodes != 1:
                # 부모 갱신
                parent[nodes] = root
                queue.append(nodes)


# BFS진행
BFS()

# 각 노드의 부모 출력
for i in range(2, n+1):
    print(parent[i])
