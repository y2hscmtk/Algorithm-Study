# https://www.acmicpc.net/problem/18809
'''
배양액 뿌릴 수 있는 땅은 미리 정해져 있다.

매 초마다 이전에 배양액이 도달한 적 없는 인접한 땅으로 퍼져나간다.(호수 제외)

초록색 배양액과 빨간색 배양액이 동일한 시간에 도달한 땅에서는 두 배양이 합쳐져 꽃이 핀다. => 동일한 시간을 판단할 수 있는 기준 설정
꽃이 피어난 땅에서는 배양액이 사라져 더이상 퍼지지 않는다.

모든 배양액을 남김 없이 사용해야 한다. => 초기에 배양액을 뿌릴 땅을 설정한 뒤 시뮬레이션을 시작한다.

정원과 두 배양액의 개수가 주어질 때, 피울 수 있는 꽃의 최대 개수 구하기

0(호수), 1(배양액 뿌릴수 없는 땅), 2(배양액 뿌릴 수 있는 땅)
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]; dy = [-1,1,0,0]

N,M,G,R = map(int,input().split()) 
earth = []; select_able = []
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(M):
        if row[j] == 2: # 배양액을 심을 수 있는 땅이라면
            select_able.append((i,j))
    earth.append(row)
    
# 1. 배양액 뿌릴 땅 선택
# 입력 단계에서 배양액을 뿌릴수 있는 땅을 선택하여 기록, 이후 초록 색 배양액과 빨간색 배양액을 적절히 선택
selected = [] # 배양액을 뿌리도록 선택된 땅 
def select_earth(curr,count):
    if count == G + R:
        # 배양액 시뮬레이션 시작
        spread_fertilizer(0,0,[False]*(G+R))
        return
    
    # 배양액을 뿌릴수 있는 땅에 대하여
    for i in range(curr,len(select_able)):
        selected.append(select_able[i])
        select_earth(i+1,count+1)
        selected.pop() # 백트래킹

# 배양액을 뿌릴 땅이 선택된 시점
# 초록색 배양액을 뿌릴 땅을 먼저 선택하고 선택하지 않은 땅에 대해서 빨강색 배양액을 뿌린다.
result = 0 # 피울 수 있는 꽃의 최대 개수
def spread_fertilizer(curr,green_count,selected_green):
    global result
    if green_count == G:
        result = max(result,start(selected_green)) # 시뮬레이션 시작
        return
    
    # i번째 땅을 초록색 배양액을 뿌리기 위한 땅으로 선택
    for i in range(curr,G+R):
        selected_green[i] = True
        spread_fertilizer(i+1,green_count+1,selected_green)
        selected_green[i] = False
        

# 초록색으로 선택된 땅은 True, 빨강색으로 선택된 땅은 False
def start(selected_green):
    queue = deque()
    visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    flowerCount = 0 # 꽃이 몇개 피었는지 확인하는 용도
    
    # 배양액이 뿌려진 땅에 대해서
    for i in range(len(selected)):
        x,y = selected[i]
        if selected_green[i]: # 초록색을 뿌리도록 선택된 땅이라면
            queue.append((x,y,0))
            visited[x][y][0] = 0
        else:
            queue.append((x,y,1))
            visited[x][y][1] = 0 
    
    # 배양액 분산 시작
    while queue:
        x,y,color = queue.popleft()
        
        # 해당 좌표에서 두 배양액이 합쳐졌다면(꽃이 피었다면), 탐색 불가
        if (visited[x][y][0] == visited[x][y][1]):
            continue
        
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 배양액이 퍼질 수 있는 공간인지 확인
            # 0. 영역을 벗어나지 않아야함
            # 1. 호수가 아니어야 함
            if 0<=nx<N and 0<=ny<M and earth[nx][ny] != 0:
                # 2. 이미 배양액이 뿌려진 곳이 아니어야 함                
                # 현재 시점 이전에 빨강색 배양액이 뿌려지지 않았는지 확인 
                if -1 < visited[nx][ny][(color+1)%2] <= visited[x][y][0]:
                    continue
                
                # 초록색 배양액이 이미 뿌려진 곳이 아니어야 함
                if visited[nx][ny][color] == -1:
                    visited[nx][ny][color] = visited[x][y][color] + 1
                    # 배양액을 뿌림으로서 꽃이 피었는지 확인
                    if visited[nx][ny][color] == visited[nx][ny][(color+1)%2]:
                        flowerCount += 1
                        continue
                    # 꽃이 피지 않았다면 탐색 수행
                    queue.append((nx,ny,color))
                    
    return flowerCount # 현재 시뮬레이션에서 핀 꽃의 개수 반환

select_earth(0,0)
print(result)