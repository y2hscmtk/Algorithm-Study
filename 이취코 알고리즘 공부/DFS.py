# https://www.youtube.com/watch?v=7C9RgOcvkvo&t=1717s

# 알고리즘 중간고사 문제 검토

def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 ( 2차원 리스트)
graph = [
    [3, 5, 8],
    [2, 4, 6],
    [1, 7],
    [0, 6, 8],
    [1, 8],
    [0],
    [1, 3, 7],
    [2, 6, 8],
    [0, 3, 4, 7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 10
# 정의된 DFS 함수 호출
dfs(graph, 6, visited)
