# https://www.acmicpc.net/problem/1260

# 백준 1260번 DFS/BFS

'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''

'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''

from collections import deque
n, m, v = map(int, input().split())

vertix = [i for i in range(1, n+1)]  # 정점의 정보를 저장할 리스트

edge = []
for _ in range(m):
    edge.append(list(map(int, input().split())))

# edge.sort()  # 오름차순으로 정렬 1번 정점부터 연결정보가 표시될것 # 굳이 오름차순 할 필요 없을듯

adj = [[] for vt in vertix]  # 정점의 개수만큼 생성

# 연결리스트 생성
for e in edge:  # 간선 리스트에서 간성정보를 한개씩 뽑아서
    adj[e[0]-1].append(e[1])  # 간선 삽입 0번 인덱스부터 삽입되어야 함
    adj[e[1]-1].append(e[0])  # 위 문제의 경우 양방향 리스트임

# 첫째줄에는 DFS를 수행한 결과 두번째 줄에는 BFS를 수행한 결과를 출력한다.

# DFS 알고리즘 : 깊이 우선 탐색
# 미로 찾기라고 생각 => 미로를 찾는것처럼 한쪽으로 갈수 있는 만큼 가다가 더이상 갈수 없게되면 가장 가까운 갈림길로 되돌아간다.
# 되돌아가야 되기때문에, 돌아갈 곳의 위치를 저장할 스택이 필요함 => 재귀호출을 통해 묵시적 스택사용이 가능하다.

stack = [v]  # 시작정점은 v임
dfs_visited = []  # 방문한 정점을 저장할 리시트
while stack:
    c = stack.pop()  # 현재위치를 의미
    dfs_visited.append(c)
    for neighbor in adj[c-1]:
        if neighbor not in dfs_visited:
            stack.append(neighbor)
            break

# BFS 알고리즘 : 너비 우선 탐색
# 가까이에 있는 정점을 먼저 방문하고, 멀리 떨어져 있는 정점을 나중에 방문한다.
# "큐"를 사용하여 구현한다.

bfs_visited = []
queue = deque()

queue.append(v)
while queue:
    c = queue.popleft()
    bfs_visited.append(c)
    for neighbor in adj[c-1]:
        if neighbor not in bfs_visited and neighbor not in queue:
            queue.append(neighbor)


for i in dfs_visited:
    print(i, end=' ')
print()
for i in bfs_visited:
    print(i, end=' ')
