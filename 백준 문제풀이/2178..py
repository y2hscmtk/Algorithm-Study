# https://www.acmicpc.net/problem/2178

'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때,
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
'''
아이디어1
오른쪽 아래를 향하는 것이 최종 목표이므로, 깊이 우선탐색을 오른쪽,아래,위로 반복하여 진행한다.
방문을 하면 해당 요소를 0으로 변경하고, 카운트를 +1 증가시킨다. 해당 정점에서 더이상 갈 수 없게 될때마다 재귀함수를 통해 탈출하고,
카운트를 -1 시킨다. 최종 결과를 마지막에 출력한다.
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # n개의 줄에 m개의 요소를 각각 입력받아 삽입

#count = 0


def dfs(graph, start, end):
    count = 0
    d, s, w, a = 0, 0, 0, 0
    global n, m
    if not ((0 <= start < n) and (0 <= end < m)):
        return count  # 해당 정점이 영역을 벗어난 경우
    if start == n-1 and end == m-1:
        return count
    if graph[start][end] == 0:
        return count
    if graph[start][end] == 1:  # 해당 정점을 방문한적이 없다면
        graph[start][end] = 0  # 방문처리
        count += 1  # 방문한 정점 +1
        d = dfs(graph, start, end+1)  # 오른쪽에 길이 있는지 탐색
        s = dfs(graph, start+1, end)  # 아래쪽에 길이 있는지 탐색
        w = dfs(graph, start-1, end)  # 위쪽에 길이 있는지 확인
        a = dfs(graph, start, end-1)  # 왼쪽에 길이 있는지 확인
    return count+d+s+w+a

    # 깊이 우선 탐색을 진행하여 목적지에 도달하기까지 방문한 정점 탐색
s, e = 0, 0
result = dfs(graph, 0, 0)

print(result)
