# 미로 탈출

# 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 동빈이의 위치는 (1,1)이고 미로의 출구는 (NxM)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 조건 : 첫째 줄에 두 정수 N,M이 주어진다. 다음 N개의 줄에는 각각 M개의 정수로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
#            또한 시작칸과 마지막 칸은 항상 1이다.
# 출력 조건 : 첫째 줄에 최소 이동 칸의 개수를 출력한다.

# 입력 예시         출력 예시
# 5 6              10
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque
# 공백으로 구분하여 n과 m 입력받기
n, m = map(int,input().split())

# 미로 정보를 입력받을 그래프 생성
graph = []
for i in range(n): # 행의 개수만큼 반복하여 미로 정보 입력받아, 그래프에 저장하기
    graph.append(list(map(int,input()))) # 각각의 정보는 정수형으로 공백없이 입력받고, list형태로 저장한다.
    
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 반복이 종료 된 이후, n,m 위치의 결과값을 반환
    return graph[n-1][m-1]

print(bfs(0,0))
    

