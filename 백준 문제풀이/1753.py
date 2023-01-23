# https://www.acmicpc.net/problem/1753

'''
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 

단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
(1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. 
u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
'''
'''
아이디어1 : 다익스트라 알고리즘으로 풀어보자
'''
# 다익스트라 알고리즘 : 한 정점에서 다른 정점까지의 최단 경로를 구하는 알고리즘
# 최단경로가 발견된 정점을 기록할 배열 found 배열, 최단경로의 길이를 저장할 배열 distance배열이 필요
# distance[i][j]는 정점 i에서 정점 j까지의 거리를 기록 => 길이 없다면 INF를 저장(무한)

# 해당문제는 단방향 그래프임에 유의

v, e = map(int, input().split())  # v정점의 개수,e간선의 개수
k = int(input())  # 탐색을 시작할 정점

graph = [[] for _ in range(v+1)]  # 그래프 간선 저장용

found = [False for _ in range(v+1)]  # 최단경로를 찾았는지에 대한 여부를 저장

# 최단경로를 저장할 배열, 탐색 시작정점에서 정점u까지의 최단경로를 distance[u]로 표현한다.
distance = ['INF']*(v+1)

for _ in range(e):
    # i에서j로 가는 길의 가중치 w
    i, j, w = map(int, input().split())
    graph[i].append([j, w])  # u에서 v로의 경로와 가중치를 저장

# 다익스트라 알고리즘

# distance배열 초기화
for node, weight in graph[k]:
    distance[node] = weight  # k에서 각 정점까지의 최단경로 초기화
distance[k] = 0  # 탐색 시작 정점은 0으로 표시
found[k] = True  # 시작정점 방문처리


# 시작정점을 기준으로 distance가 가장 작은 정점 u를 찾아 리턴
def choose():
    global distance, found
    min_weight = (v+1)*10  # 가중치 w는 최대 10, 모든 정점을 지나갈경우의 최대가중치 10+10+10...
    min_index = -1  # distance가 가장 작은 정점의 인덱스 리턴
    for i in range(1, v+1):
        # 해당정점으로의 길이 없다면 다음정점에서 탐색
        if distance[i] == 'INF':
            continue
        # found배열에 소속되어있지 않으면서 가중치가 최소인 정점 탐색
        if distance[i] < min_weight and not found[i]:
            min_weight = distance[i]  # 최소 가중치 갱신
            min_index = i  # 인덱스 저장
    return min_index


# 다익스트라 알고리즘 시작
for i in range(1, v+1):
    u = choose()  # 현재 distance에 기록된 정점중 최소가중치의 정점
    found[u] = True  # found 처리(최단경로 탐색성공)
    # distance배열의 값 업데이트
    # 정점 u를 통해서 가는 길이 기존의 경로보다 작은값일때 업데이트
    for j in range(1, v+1):
        if not found[j]:  # 아직 found되지 않은 정점에 대하여
            # 기존의 최단경로를 기록할 배열 생성
            # u에서 각 정점까지의 경로를 저장 => weight[1] => u에서 1번 노드까지의 가중치
            weight = ['INF']*(v+1)
            for n, w in graph[u]:
                weight[n] = w  # 값 저장
            if weight[j] == 'INF':
                continue  # u에서 j로의 경로가 없다면 다음 노드부터탐색
            # u를 거쳐가면 기존의 경로보다 길이 단축되는지 확인
            if distance[j] == 'INF':
                distance[j] = distance[u] + weight[j]  # 기존에 경로가 없었다면 업데이트
                continue
            # 기존에 경로가 있다면 길이 비교
            if distance[u] + weight[j] < distance[j]:
                distance[j] = distance[u] + weight[j]  # 최단경로 업데이트

# 결과 출력
for i in range(1, v+1):
    print(distance[i])
