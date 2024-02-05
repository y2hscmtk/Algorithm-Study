from collections import deque
'''
이분 그래프 => 인접한 정점을 서로 다른 색으로 칠할 수 있는 그래프

<이분 그래프>          <이분 그래프x>
1(R) -  3(B)        1(R) - 2(B)
        |                /   |
        2(R)        3(R) - 4(R)
        
두번재 예시의 경우 4는 인접한 정점 3과 같은 색으로 칠해지므로 이분 그래프가 될 수 없다.
'''
def isBinaryGraph(start):
    queue = deque([start])
    visited[start] = 1 # 1번 노드는 색상코드 1로 기입
    while queue:
        node = queue.popleft()
        # 인접 노드에 대해서 탐색 수행
        for iNode in graph[node]:
            # 인접 노드 중에 방문했던 적이 있는 노드가 존재한다면 현재 자신의 색과 같은지 비교
            if visited[iNode] != 0:
                if visited[iNode] == visited[node]:
                    # 현재 자신의 색과 같다 -> 인접 노드가 같은 색으로 칠해졌다 -> 이분그래프 불가능
                    return False
            else: # 방문한 적이 없는 노드에 대해
                visited[iNode] = -(visited[node]) # 현재 색과 다른 색상으로 기록
                queue.append(iNode)
    return True # 문제없이 끝까지 수행하였다면 이분그래프가 가능함

for _ in range(int(input())):
    v,e = map(int,input().split())
    visited = [0]*(v+1) # 0방문한적 없는 노드, 1,-1은 색상
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # 그래프가 모두 연결되어있지 않을 수 있음 - 연결되지 않은 그래프
    isBinary = True
    for v in range(1, v+1):
        if visited[v] == 0:  # 방문하지 않은 노드에서 BFS 시작
            if not isBinaryGraph(v):
                isBinary = False
                break

    print("YES" if isBinary else "NO")