# https://www.acmicpc.net/problem/2583

from collections import deque


def append_queue(queue, start, end):
    queue.append([start+1, end])
    queue.append([start, end+1])
    queue.append([start-1, end])
    queue.append([start, end-1])


def bfs(graph, start, end):
    global m, n, counts, index
    queue = deque()
    graph[start][end] = 0  # 방문처리
    counts[index] += 1  # 넓이 +1
    append_queue(queue, start, end)
    while queue:
        data = queue.popleft()
        s, e = data[0], data[1]
        if 0 <= s < m and 0 <= e < n:
            if graph[s][e] == 1:  # 아직 방문하지 않았다면
                graph[s][e] = 0  # 방문처리하고
                counts[index] += 1  # 넓이 +1
                append_queue(queue, s, e)


m, n, k = map(int, input().split())

# 1은 갈수 있는 경로라는 의미 0은 길이 없다는 의미
# 그래프의 모든 노드값을 1로 초기화하여 그래프를 생성한다.
graph = [[1 for _ in range(n)] for _ in range(m)]


# k개의 사각형 좌표 입력받기 => 갈수 있는 영역과 갈수 없는 영역 정하기
for _ in range(k):
    y, x, y2, x2 = map(int, input().split())
    for i in range(x, x2):
        for j in range(y, y2):
            graph[i][j] = 0  # 사각형 공간으로 채운다.

counts = []
index = -1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:  # 새로운 그룹을 발견했다면
            index += 1
            counts.append(0)  # 영역의 넓이를 저장하기 위해 요소 추가
            bfs(graph, i, j)  # 탐색 시작


print(len(counts))  # 영역의 개수를 출력한 후
counts.sort()  # 오름차순으로 정렬시킨후
# 공백으로 영역의 넓이를 출력한다.
for count in counts:
    print(count, end=' ')
