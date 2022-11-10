# https://www.acmicpc.net/problem/2468

'''
장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 
위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다. 
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 
'''


'''
아이디어 1
높이에 따라 물에 잠기는 지형이 달라지므로 그에 따른 그룹의 개수가 달라진다.
따라서 높이를 달리하며 해당 숫자보다 높이가 작은 경우 길이 없는것으로 간주하며 그래프 탐색을 진행하면 될듯하다.
'''

from collections import deque
import copy # 2차원 배열 복사를 위함
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]


def append_queue(queue, start, end):
    queue.append([start+1, end])
    queue.append([start-1, end])
    queue.append([start, end+1])
    queue.append([start, end-1])


def bfs(graph, start, end, height):
    global n
    graph[start][end] = height  # 해당 높이보다 작을 경우 방문할수 없음을 의미 => 방문처리
    queue = deque()
    append_queue(queue, start, end)  # 인접 정점 방문처리
    while queue:
        data = queue.popleft()
        s, e = data[0], data[1]
        if 0 <= s < n and 0 <= e < n:  # 영역을 벗어나지 않으면서
            if graph[s][e] > height:  # 방문할수 있는 곳이라면
                graph[s][e] = height  # 방문하고
                append_queue(queue, s, e)  # 인접 정점들 탐색


# 입력받은 데이터에서 최고 높이 탐색을 위함
maxHeight = 1

for i in range(n):  # 그래프에서 최고높이와 최저높이 탐색
    maxTemp = max(graph[i])
    if maxHeight <= maxTemp:
        maxHeight = maxTemp

maxCount = 0
# 높이를 달리하며 그래프 탐색 시작
for h in range(maxHeight+1):  # 최소높이부터 최대높이까지 탐색
    count = 0
    graphCopy = copy.deepcopy(graph)  # 원본 그래프 훼손을 막기 위함 => 깊은 복사를 해주어야함
    for i in range(n):
        for j in range(n):
            if graphCopy[i][j] > h:  # 최소높이부터 탐색시작
                count += 1  # 새로운 그룹 발견 => 카운트 증가
                bfs(graphCopy, i, j, h)
    # 탐색 종료 이후 count를 비교하여 max카운트 찾기
    if maxCount <= count:
        maxCount = count  # 그룹의 개수가 더 많으면 그 값으로 변경

print(maxCount)
