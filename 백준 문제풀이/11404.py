# https://www.acmicpc.net/problem/11404
'''
플로이드 워셜
모든 정점에 대해서, 다른 정점을 거쳐갔을때 코스트가 더 줄어드는지 확인하여 갱신한다.
3중 반복문 => O(v^3)
'''
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]  # 1부터 시작
for _ in range(int(input())):
    # 시작 도시와 도착 도시가 같은 경우는 없다
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # a에서 b지역을 가는데 비용 c가 든다.

# 정답용 2차원 그래프 생성 => N x N 크기
INF = int(1e9)
array = [[INF]*(n+1) for _ in range(n+1)]


def floyd():
    global array
    # 자기 자신으로의 비용은 0원
    for i in range(1, n+1):
        array[i][i] = 0

    # 기존 최단경로 초기화
    for i in range(len(graph)):
        # i에서 갈 수 있는 경로와 비용에 대해
        for cost, destiny in graph[i]:
            # 비용 갱신이 가능하다면 갱신
            if cost < array[i][destiny]:
                array[i][destiny] = cost

    # 모든 정점에 대해서
    for v in range(1, n+1):
        # 해당 정점을 통해서 지나갈때 비용이 감소한다면 갱신
        for i in range(1, n+1):
            for j in range(1, n+1):
                # v를 거쳐가는 경로가 더 비용이 적게 든다면 갱신
                array[i][j] = min(array[i][j], (array[i][v] + array[v][j]))


floyd()

# 정답 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if array[i][j] == INF:
            print(0, end=' ')
        else:
            print(array[i][j], end=' ')
    print()
