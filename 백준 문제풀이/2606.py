# https://www.acmicpc.net/problem/2606

'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

7
6
1 2
2 3
1 5
5 2
5 6
4 7

'''
'''
아이디어 1
네트워크를 그래프를 통해 구성하고, 정점 1에서부터 깊이 우선 탐색, 혹은 너비 우선 탐색을 진행한다.
탐색이 끝난 후 모든 정점에 대해 방문 기록이 있는지 확인하고 방문 기록이 있다면 바이러스에 감연된것으로 간주,
방문 기록이 없다면 같은 그룹에 속한 네트워크가 아니므로 넘어간다.
알고리즘이 종료 된 이후 결과를 출력한다.
'''


from collections import deque
result = 0  # 바이러스에 감염된 컴퓨터의 수

vertix = int(input())  # 컴퓨터의 수 : 정점의 개수
edge = int(input())  # 연결되어 있는 쌍의 수 : 간선의 개수

network = [[] for _ in range(vertix+1)]  # 정점의 개수만큼 생성
visited = [False for _ in range(vertix+1)]  # 정점의 방문체크

for i in range(edge):
    start, end = map(int, input().split())  # 시작정점, 끝 정점 입력받고
    network[start].append(end)  # 해당 정점정보 입력
    network[end].append(start)  # 양방향으로~

# 탐색 진행 : 큐를 활용하여 너비우선 탐색 진행
queue = deque()  # 1번 정점의 간선들을 큐에 삽입
for v in network[1]:
    queue.append(v)

# 너비 우선 탐색 큐에 담겨진 데이터가 없을때까지 진행
while queue:
    v = queue.popleft()  # 정점을 하나씩 뽑아가며 탐색
    if visited[v]:  # 해당정점을 방문한 경우
        continue  # 다음 정점을 뽑는다
    # 해당 정점을 방문하지 않은 경우에 대하여
    visited[v] = True  # 정점 방문처리
    for c in network[v]:
        queue.append(c)  # 해당 정점의 간선들 입력

for visit in visited:
    if visit:
        result += 1

print(result-1)
