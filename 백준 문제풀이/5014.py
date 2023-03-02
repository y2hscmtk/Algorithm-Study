# https://www.acmicpc.net/problem/5014

'''
첫째 줄에 F, S, G, U, D가 주어진다. 
(1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 
가장 높은 층은 F층이다.

총 F층으로 구성된 건물에서 G층에 도달하는것이 목표
현재 위치는 S, U버튼은 누를경우 U만큼 위로 이동하고, D버튼은 누르면 D만큼 아래로 이동함

출력
첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다
'''
from collections import deque

F, S, G, U, D = map(int, input().split())

# visited배열을 만들어서 이동하는 횟수를 기록
visited = [-1]*(F+1)

# use the stairs

# S에서 G위치에 도달하는것이 목표

# bfs 정의
# 버튼의 최소횟수 정의


def bfs():
    queue = deque()
    queue.append(S)  # 시작위치 지정
    visited[S] = 0  # 시작위치 0으로 설정
    while queue:
        node = queue.popleft()

        if node == G:  # 인덱스이기 때문에, -1
            # 목적지에 도달하였다면 탐색 종료
            return visited[node]

        # 두 가지 방향에 대해 방문 정의(위로 U만큼 가거나, 아래로 D만큼 가거나)
        for move in [+U, -D]:
            next_node = node + move
            # 방문한적 없다면, 그리고 영역을 벗어나지 않는다면
            if 0 < next_node <= F:
                if visited[next_node] == -1:
                    visited[next_node] = visited[node] + 1  # 버튼 푸쉬횟수 증가
                    queue.append(next_node)  # 큐에 삽입
    return "use the stairs"


print(bfs())
