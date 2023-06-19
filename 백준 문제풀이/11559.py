# https://www.acmicpc.net/problem/11559
'''
같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
'''
'''
아이디어1
더이상 터뜨릴수 없을때 까지, 반복문을 통해 bfs를 수행한다.
bfs를 수행하면서 같은 색 블록은 전부 .으로 변경하고, 이후 .위에 .이 아닌 문자가 있는지 확인하여 위의 블록을 아래로 끌고 내려온다.(swap)
다시 새롭게 생성된 게임판을 다시 반복문을 돌면서 bfs를 수행한다.
'''
from collections import deque

graph = [list(input()) for _ in range(12)] # 게임 맵은 12줄로 이루어져 있음

# 연쇄 회수를 저장하기 위한 변수 => 정답
result = 0
# 상하좌우 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]


# bfs 정의
def remove_puyo(s,e):
    global graph,visited
    
    visited[s][e] = True # 방문처리
    
    queue = deque()
    queue.append([s,e])
    
    # 같은 색의 뿌요를 저장하기 위한 큐
    puyo = deque()
    puyo.append([s,e]) 
    
    color = graph[s][e] # 뿌요 색 저장
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않았고 '.'이 아닌지 확인, 방문한적 없는지 확인
            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny]:
                if graph[nx][ny] == '.':
                    continue
                # .이 아닌 경우에 대해서만 같은색인지 확인
                if graph[nx][ny] == color: # 같은 색이고 방문하지 않았다면
                    puyo.append([nx,ny])
                    visited[nx][ny] = True # 방문처리
                    queue.append([nx,ny]) # 큐에 삽입
    # 같은색 탐색이 끝난 후, 해당색 전부 제거(뿌요 큐 이용)
    # 뿌요가 4개 이상인 경우에 한해서만(4개 이하라면 제거 실패)
    if len(puyo) < 4:
        return False # 제거 실패
    # 4개 이상의 뿌요에 대해서는 제거 작업 수행
    for x,y in puyo:
        graph[x][y] = '.' # 빈공간으로 만들기
    return True # 제거 성공을 의미


# 맵 정리하는 함수(중력 적용)
def refactoring():
    global graph
    # 각 세로줄에 대해서 '.'이 아닌 문자를 모두 큐에 삽입후, 아래로 내린다(중력 적용)
    for i in range(6):
        puyo = deque([]) # 뿌요를 담을 큐
        for j in range(11,-1,-1): 
            if graph[j][i] != '.': # 뿌요라면
                puyo.append(graph[j][i]) # 해당 좌표 삽입(아래로 내리기 위해)
        
        # 아래로 내리기 작업 수행
        for p in range(len(puyo)):
            graph[11-p][i] = puyo[p] # 아래로 내리기(차곡 차곡 쌓기)
        # 쌓인 뿌요들 위는 빈 공간으로 변경
        for p in range(12-len(puyo)):
            graph[p][i] = '.'
# 전체 반복문 수행하면서 더이상 제거할게 없을때 까지 반복 수행
while True:
    remove = False # 제거 작업이 이뤄졌는지 확인
    
    # 방문정보를 저장하기 위한 배열 초기화
    visited = [[False]*6 for _ in range(12)]
    
    # 반복문을 돌면서 '.'이 아닌 문자에 대해서 bfs 수행
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                if(remove_puyo(i,j)):
                    remove = True
    
    # 한번이라도 제거 작업이 이뤄졌다면
    if remove:
        # 중력을 적용시키고
        refactoring()
        result+=1 # 연쇄 1 증가
    else: # 제거 작업이 이뤄지지 않았다면 => 더이상 제거할 것이 없다는 의미
        break # 반복 탈출
    
print(result) # 연쇄 횟수 출력