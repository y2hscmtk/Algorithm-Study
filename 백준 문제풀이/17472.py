# https://acmicpc.net/problem/17472
'''
1. 섬 분리, 섬의 끝단 저장
2. 섬의 끝단에서 다른 섬이나 벽을 만날때까지 네 방향으로 이동하여 각각 경로와 이동거리 저장
3. 각 섬에 대한 최단 거리를 저장해두고 가중치를 갖는 간선으로 삼는다.
4. 각 간선들에 대해 최소 스패닝 트리를 찾는다.
'''
import sys
from collections import deque
dx = [0,0,-1,1]; dy = [-1,1,0,0]
N,M = map(int,input().split()) # 세로 N 가로 M
visited = [[False]*M for _ in range(N)]
graph = [list(map(int,input().split())) for _ in range(N)]
island_num = 0 # 섬의 식별 번호
end_point = [] # 섬의 끝단 => 다리 짓기에 사용
bridge = {}
edges = [] # 간선들을 저장하기 위한 배열 
# 각 섬을 구별
def find_island(s,e):
    global visited,graph
    queue = deque([(s,e)])
    graph[s][e] = island_num
    visited[s][e] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                # 땅(1)인 경우에 대해서 방문처리
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = island_num
                    queue.append((nx,ny))
                # 상하좌우 중 한 곳이 0이라면 현재좌표(x,y)는 섬의 끝단
                elif graph[nx][ny] == 0:
                    end_point.append([x,y,island_num])

# 섬 구별 짓기
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1: # 새롭게 땅을 발견한다면
            island_num+=1
            find_island(i,j)

parent = [i for i in range(island_num+1)] # 섬의 개수 만큼 생성(유니온 확인용)

# 해당 집합에 대한 루트 노드 찾기
def find_parent(x):
    global parent
    # 자기 자신과 같은 경우 루트 노드임
    if x!=parent[x]:
        parent[x] = find_parent(parent[x]) # parent[x]에 부모노드 직접 삽입하는 효과 -> 경로 압축
    return parent[x]

# 섬의 모든 끝단에서 다리 짓기 시작
for x,y,num in end_point:
    # 현재 위치에서 한 방향 끝으로 쭉 이동
    for i in range(4):
        length = 0 # 다리 길이
        nx,ny = x,y
        while True:
            nx += dx[i]; ny += dy[i]
            # 이동 가능한지 확인
            if nx<0 or nx>=N or ny<0 or ny>=M:
                break
            # 만약 이동하게 된 곳이 현재 숫자와 똑같다 => 다리를 지을 수 없음(섬 내부임)
            if graph[nx][ny] == num:
                break
            # 이동 가능하다(물이다)
            elif graph[nx][ny] == 0:
                length += 1 # 섬 길이 증가
            # 다른 섬에 도착하였다.
            elif graph[nx][ny] != 0 and graph[nx][ny] != num:
                # 다리는 길이가 2이상
                if length < 2:
                    break
                edges.append((length,num,graph[nx][ny]))
                break
                # if num<graph[nx][ny]:
                #     key = f'{num},{graph[nx][ny]}'
                # else:
                #     key = f'{graph[nx][ny]},{num}'
                # # 현재까지 지어진 다리 거리 저장
                # if key not in bridge:
                #     bridge[key] = [length] # key 경로로 갈때의 COST
                # else:
                #     bridge[key].append(length)


# # 생성한 키들을 바탕으로 간선 생성
# for key in bridge:
#     bridge[key].sort() # 오름차순 정렬
#     s,e = map(int,key.split(','))
#     edges.append((bridge[key][0],s,e)) # 0번째 값이 가장 작으므로 코스트가 된다.

# 크루스칼 알고리즘 수행
'''
간선 집합을 코스트를 기준으로 정렬한다.
가장 코스트가 낮은 간선부터 차례로 꺼내고, 해당 간선을 기존 집합에 이었을때 순환집합이 완성되는지 확인한다.
만약 순환집합이 되지 않는다면 새로 추가할 수 있으므로 두 집합(시작 노드 집합,끝 노드 집합)을 하나로 합한다.
'''
edges.sort()
result = 0 # 모든 섬을 이었을때 간선의 최소치
count = 0 # 간선을 총 몇개 선택하였는지 확인
for cost,s,e in edges:
    s_parent = find_parent(s)
    e_parent = find_parent(e)
    if s_parent!=e_parent: # 두 부모가 같지 않다 => 현재 간선을 추가할 수 있다.
        # 간선을 추가함으로서, 두 집합이 이어진다.
        if s_parent < e_parent: # 집합의 루트노드는 가장 작은 값으로 설정하도록 한다.
            parent[e_parent] = s_parent # e정점 집합의 루트를 s정점 집합의 루트로 설정 => 하나의 집합이 된 효과
        else:
            parent[s_parent] = e_parent
        result += cost # 현재 간선을 추가하였으므로 cost 증가
        count += 1 # 간선 선택

# island_num-1개의 간선 선택시 최소스패닝트리 가능
print(result if count == island_num-1 else -1)