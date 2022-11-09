# https://www.acmicpc.net/problem/4963


from collections import deque
w, h = 0, 0


def append_queue(queue, start, end):  # 인접한 정점들 큐에 삽입
    queue.append([start+1, end])
    queue.append([start, end+1])
    queue.append([start-1, end])
    queue.append([start, end-1])


def bfs(graph, start, end):
    global w, h
    # 현재 입력된 정점 방문처리
    graph[start][end] = 0
    queue = deque()
    append_queue(queue, start, end)  # 인접 정접 삽입
    while queue:  # 큐에 데이터가 있는동안 반복
        data = queue.popleft()
        s, e = data[0], data[1]  # 좌표 뽑기
        if 0 <= s < h and 0 <= e < w:  # 범위를 벗어나지 않을때
            if graph[s][e] == 1:  # 해당 정점 방문 안했다면
                graph[s][e] = 0  # 방문처리
                append_queue(queue, s, e)  # 인접정접 삽입


# 0,0이 입력되면 종료 1은 땅, 0은 바다를 의미, # 섬의 개수를 파악하는것이 문제
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    count = 0  # 섬의 개수
    # h는 높이 w는 너비 => graph[h][w] 순으로 표현
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:  # 새로운 땅을 발견시
                count += 1  # 새로운 섬을 발견했다는 의미로 카운트 증가
                bfs(graph, i, j)  # 너비 우선 탐색 시작
    print(count)  # 탐색 종료 이후 섬의 개수 출력
