# https://www.acmicpc.net/problem/2606
'''
1번 컴퓨터에서 bfs수행
해당 그룹의 수를 출력
'''
from collections import deque
n = int(input())

# 해당 인덱스의 번호와 연결된 노드들을 저장
# graph[1] = [2,3] //1번 노드에 2,3노드가 연결되어있음을 의미
graph = [[] for _ in range(n+1)]

# 간선 정보 저장
for _ in range(int(input())):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
# 즉, 1번 컴퓨터는 그룹 카운트에 포함되지 않는다.
def bfs():
    # 탐색은 1번 노드에서 시작
    # 아직 방문하지 않은 정점에 대해서 bfs를 수행
    visited = [1] # 방문한 노드를 저장할 배열
    queue = deque()
    queue.append(1) # 탐색을 시작할 노드
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if n not in visited: # 아직 방문한 적 없다면
                visited.append(n) # 방문처리
                queue.append(n) # 큐에 삽입
    return len(visited)-1 # 1번 노드는 정답에서 제외됨

print(bfs())
