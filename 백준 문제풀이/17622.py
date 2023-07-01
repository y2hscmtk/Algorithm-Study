# https://www.acmicpc.net/problem/17622
# 정수 N(2 ≤ N ≤ 50)과, 교체할 수 있는 타일의 개수를 나타내는 k(0 ≤ k ≤ 1)가 주어진다. 

# 이동할수 있는 타일을 미리 제작 => 방향 벡터로 이용
'''
       [-1,0]
[0,-1] [0,0] [0,1]
       [1,0]
'''
from collections import deque
import sys
# 타일 배열의 각 인덱스에서 
# 첫번째 배열 => dx
# 두번째 배열 => dy
# 0번 타일(아래,오른쪽)
num0 = [[1,0],[0,1]]
# 1번 타일(왼쪽,아래)
num1 = [[0,1],[-1,0]]
# 2번 타일(위,오른쪽)
num2 = [[-1,0],[0,1]]
# 3번 타일(왼쪽,위)
num3 = [[0,-1],[-1,0]]
# 4번 타일(위,아래)
num4 = [[-1,1],[0,0]]
# 5번 타일(왼쪽,오른쪽)
num5 = [[0,0],[-1,1]]

tile = [num0,num1,num2,num3,num4,num5]


# 0번 타일은 아래는 2,3,4, 오른쪽은 5번 타일만 가능
can0 = [[2,3,4],[5]]
# 1번 타일은 왼쪽은 0,2,5, 아래는 2,3,4번 타일만 가능
can1 = [[0,2,5],[2,3,4]]
# 2번 타일은 위쪽은 0,1,4, 오른쪽은 1,3,5번 타일만 가능
can2 = [[0,1,4],[1,3,5]]
# 3번 타일은 왼쪽은 0,2,5, 위쪽은 0,1,4번 타일만 가능
can3 = [[0,2,5],[0,1,4]]
# 4번 타일은 위쪽은 0,1,4, 아래쪽은 2,3,4번 타일만 가능
can4 = [[0,1,4],[2,3,4]]
# 5번 타일은 왼쪽은 0,2, 오른쪽은 1,3,5번 타일만 가능
can5 = [[0,2],[1,3,5]]

tile_candidate = [can0,can1,can2,can3,can4,can5]



# nxn 크기의 격자, k개 변경할수있음(0<=k<=1)
n,k = map(int,input().split())
# 현재 지도 상황
graph = [list(map(int,input().split())) for _ in range(n)]
'''
# bfs로 시작 좌표에서 끝 좌표(목적지로) 이동
# 이동하는 방향벡터는 각 타일의 번호를 보고 결정
# 방문처리를 위한 visited배열 필요
# k가 0이라면 처음과 끝을 이을 수 있는지 한번의 bfs로 확인한다.
# k가 1이라면
# 타일을 하나씩 변경해가며 이동이 가능한지 시도(브루트포스)
# => n*n*6번 변경해야하며 최대 15000번에 해당,
# 15000번의 bfs를 수행 => 15000 * 50*50*2 = 75,000,000 ??
'''
def bfs():
    count = 0 # 몇개의 타일을 사용했는지 카운트
    queue = deque()
    queue.append([0,0]) # 탐색을 시작할 좌표
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True # 시작 좌표는 방문처리
    # 시작 타일이 0,2,4인 경우, 시작부터 이동이 불가능
    num = graph[0][0]
    if num == 0 or num == 2 or num == 4:
        return -1 # 타일을 바꿔서 다시 와야함
    while queue:
        x,y = queue.popleft()
        # 목적지에 도달하였다면 bfs 종료
        # 목적지는 마지막 타일이 아님에 주의
        # 마지막 타일의 좌표 => (n-1,n-1), 따라서 목적지는 (n-1,n)
        # 현재 좌표의 타일로, 목적지에 도달할수있는지 확인하고, 도달할수 있다면 카운트 출력
        # 현재 그래프에 놓여진 타일로 이동가능한 방향벡터 결정
        num = graph[x][y]
        dx = tile[num][0]
        dy = tile[num][1]
        if x==n-1 and y==n-1:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                # 목적지에 도달할 수 있다면
                if nx == n-1 and ny == n:
                    count += 1
                    return count
            return -1
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            # 아직 방문하지 않았고, 배열의 영역을 벗어나지 않는
            # 해당 타일로 이동가능한 좌표로 이동
    
            # 타일을 변경한다고 모두 이동 가능한 것은 아님
            # 다음 타일에서 해당 길이 가능해야함
            # 0번 타일은 아래는 2,3,4, 오른쪽은 5번 타일만 가능
            # 1번 타일은 왼쪽은 0,2,5, 아래는 2,3,4번 타일만 가능
            # 2번 타일은 위쪽은 0,1,4, 오른쪽은 1,3,5번 타일만 가능
            # 3번 타일은 왼쪽은 0,2,5, 위쪽은 0,1,4번 타일만 가능
            # 4번 타일은 위쪽은 0,1,4 아래쪽은 2,3,4번 타일만 가능
            # 5번 타일은 왼쪽은 0,2, 오른쪽은 1,3,5번 타일만 가능
            # 이동가능한 번호 목록
            candidate = tile_candidate[num][i]
            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 다음에 이동할 타일의 번호 확인
                next_num = graph[nx][ny]
                if next_num in candidate: # 이동 가능한 번호 목록에 있다면 이동
                    visited[nx][ny] = True # 이동
                    queue.append([nx,ny]) # 값 삽입
                    count += 1 # 사용한 타일 수 카운트
    return -1 # 목적지에 도달하지 못할경우

# 바꿀수 있는 타일의 수가 없다면, 한번의 bfs로 결과를 출력
if k==0:
    print(bfs())
else: # k==1
    result = sys.maxsize
    # 모든 타일을 한번씩 다른것으로 바꿔본다.
    for i in range(n):
        for j in range(n):
            num = graph[i][j]
            for m in range(5):
                # 자기 자신의 번호로는 바꾸지 않는다.
                if m==num:
                    continue
                graph[i][j] = m # 다른 숫자로 바꾼후,bfs를 시켜본다
                temp = bfs()
                if temp != -1: # 탐색 실패가 아닌경우
                    result = min(result, temp) # 최소값 쳬택
            graph[i][j] = num # 백 트래킹
    # 브루트포스 이후, result가 여전히 maxsize라면 => 탐색에 실패했음을 의미
    print(result) if result != sys.maxsize else print(-1)