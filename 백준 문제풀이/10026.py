# https://www.acmicpc.net/problem/10026

'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. 
(빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
'''

'''
아이디어1

한 정점을 기준으로, 해당 정점을 아직 방문하지 않았을경우, 인접정점들을 모두 탐색하여 같은 값을 갖고 있는지 파악한다
=> 같은 값을 가지고 있다면 같은 색의 영역이라는 의미이므로 카운트를 증가 시킨다. 
RGB와 차별성을 두기 위해 방문한 정점은 X라는 키워드로 값을 변경시키고 적록색약인 사람이 탐색한 결과도 표현해야하므로
깊은 복사를 통해 배열을 복사해서 진행한다.
'''


from collections import deque
import copy
n = int(input())


def append_queue(queue, start, end):
    queue.append([start+1, end])
    queue.append([start-1, end])
    queue.append([start, end+1])
    queue.append([start, end-1])


def bfs(graph, start, end):
    global n
    color = graph[start][end]  # 색 정보 저장
    graph[start][end] = 'X'  # 방문처리
    queue = deque()
    append_queue(queue, start, end)  # 인접 정점 삽입
    while queue:
        data = queue.popleft()
        s, e = data[0], data[1]
        if 0 <= s < n and 0 <= e < n:  # 영역을 벗어나지 않고,
            if graph[s][e] == color:  # 같은 색 영역이라면
                graph[s][e] = 'X'  # 방문처리
                append_queue(queue, s, e)


graph = [list(input()) for _ in range(n)]

graph_abnormal = copy.deepcopy(graph)  # 적록색약인 사람이 이용할 그래프

for i in range(n):
    for j in range(n):
        if graph_abnormal[i][j] == 'G':
            graph_abnormal[i][j] = 'R'  # R과 G를 구별하지 못하므로 같은 문자로 변경한다.

count = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != 'X':  # 방문하지 않은 정점이라면 => 새로운 그룹이라면
            count += 1
            bfs(graph, i, j)
        if graph_abnormal[i][j] != 'X':
            count2 += 1
            bfs(graph_abnormal, i, j)
print(count, count2)
