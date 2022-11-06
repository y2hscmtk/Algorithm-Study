# https://www.acmicpc.net/problem/2667

'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
'''

'''
아이디어
각 정점에 대해서 해당 정점이 0이 아니라면 BFS를 진행하고 해당 BFS를 진행한 기록을 남긴다.
다른 정점에 대해서 방문하지 않은 정점이라면 다른 그룹이라는 의미이고, 다른 그룹이라는 의미로 카운트를 증가시킨다.
'''
from collections import deque
n = int(input())

group = []
count = []
graph = [list(input()) for _ in range(n)]  # 일부러 문자열로 입력받기

group_num = 1
queue = deque()

# 인접한 정점들을 큐에 삽입하는 메소드


def append_queue(queue, s, e):
    queue.append([s+1, e])
    queue.append([s, e+1])
    queue.append([s-1, e])
    queue.append([s, e-1])


def bfs(graph, s, e):
    global queue, n, group_num
    group.append(group_num)  # 해당 번지수 건물을 탐색하였음을 의미
    count.append([1])  # 해당 번지수의 현재 단지수를 의미한다. count[group_num-1]
    graph[s][e] = group_num
    # 인접한 정점을 큐에 삽입
    append_queue(queue, s, e)
    while queue:
        data = queue.popleft()
        start = data[0]
        end = data[1]
        if 0 <= start < n and 0 <= end < n:  # 영역을 벗어나는 경우 무시
            if graph[start][end] == '1':  # 아직 방문하지 않은 경우에 대해
                # if graph[start][end] == '0' or graph[start][end] in group:  # 0인 경우, 이미 탐색한 경우 => 탐색하지 않음
                #     continue  # 무시
                # '1'인 경우 탐색 진행
                graph[start][end] = group_num  # 번지수를 붙여주고 => 방문했음을 의미
                count[group_num-1][0] += 1
                append_queue(queue, start, end)  # 인접한 정점들을 큐에 넣어서 bfs를 진행한다.


for i in range(n):
    for j in range(n):
        # 0,0부터 탐색 시작
        # 그룹에 속해있지 않은 번지수의 건물이어야 함 => 탐색 시 방문하지 않았다는 의미
        if graph[i][j] == '1':
            bfs(graph, i, j)
            group_num += 1

count.sort()  # 오름차순으로 정렬
print(group_num-1)  # 몇 가구가 존재하는지 출력
for i in count:
    print(i[0])
