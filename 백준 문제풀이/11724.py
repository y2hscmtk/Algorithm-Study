# https://www.acmicpc.net/problem/11724

'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
'''

'''
아이디어1
네트워크 그룹의 개수를 묻는 문제이다.
탐색을 진행하여 그룹의 개수를 파악한다.
'''


from collections import deque
n, m = map(int, input().split())  # 정점, 간선의 개수

graph = [[] for i in range(n+1)]  # 인덱스 정점에서 갈 수 있는 정점을 요소로 갖는다.
visited = [False for i in range(n+1)]  # 해당 정점 방문 정보
count = 0  # 그룹의 개수를 파악

# 사용자로부터 입력받은 간선 정보를 삽입
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def bfs(graph, s):  # 깊이 우선 탐색으로 진행
    global visited
    queue = deque()
    visited[s] = True  # 해당 정점 방문처리
    for n in graph[s]:
        queue.append(n)  # 탐색을 시작할 정점의 인접 노드를 삽입
    while queue:
        node = queue.popleft()  # 정점을 하나 팝해서
        if not visited[node]:  # 해당 정점을 방문한적 없다면
            visited[node] = True  # 방문처리
            for n in graph[node]:
                queue.append(n)  # 해당 정점의 인접 정점들 방문처리


# 1번 정점부터 n번 정점까지 정점을 하나씩 뽑아가며 탐색을 진행
for i in range(1, n+1):  # 1부터 n번 정점까지 탐색 진행
    if not visited[i]:  # 해당 정점을 방문하지 않았다면 새로운 그룹
        count += 1  # count를 +1시킨다.
        bfs(graph, i)  # i 정점에서부터 탐색을 진행

print(count)
