# https://www.acmicpc.net/problem/4485
'''
INF 2차원 배열 생성하여, 각 좌표에 대한 최단 거리 갱신
시작 좌표에서 인접한 좌표들 최소힙에 삽입해서, 최단거리 노드 뽑아내기
뽑아온 노드로부터, 상하좌우 검사하여 거리 갱신(더 짧은 거리라면) 후 갱신되면 최소힙에 삽입
목적지에 도달할때까지 반복
'''
import heapq
INF = int(1e9)  # 무한 거리
t = 1  # 현재 몇번째 문제인지 기록
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dijkstera():
    global distance
    queue = []  # 최소 힙으로 사용하기 위한 배열
    # 시작 좌표에서의 가격, 시작 좌표를 최소 힙에 삽입
    heapq.heappush(queue, (graph[0][0], 0, 0))
    while queue:
        dist, x, y = heapq.heappop(queue)  # 가장 코스트가 적은 노드 뽑기
        # 네 가지 방향에 대해서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않으면서
            if 0 <= nx < n and 0 <= ny < n:
                # 현재 점을 거쳐서 가면 더 짧아진다면 갱신
                if dist + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + graph[nx][ny]
                    # 최소힙에 푸쉬
                    heapq.heappush(queue, (distance[nx][ny], nx, ny))
                # 목적지에 도달하였다면
                if (nx, ny) == (n-1, n-1):
                    return


while True:  # 0이 입력될때까지 반복
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 각 좌표에 대한 최단 경로를 저장하기 위한 배열 생성
    distance = [[INF]*n for _ in range(n)]
    # 다익스트라 알고리즘 수행
    dijkstera()
    # 정답 출력
    print(f"Problem {t}:", distance[n-1][n-1])
    t += 1
