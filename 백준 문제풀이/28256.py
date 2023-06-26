# # https://www.acmicpc.net/problem/28256
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 초콜릿 그룹 탐색
def bfs(s,e):
    global graph,result
    count = 1 # 인접한 초콜릿 개수
    queue = deque()
    queue.append([s,e])
    graph[s][e] = 'X' # 방문처리
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<3 and 0<=ny<3:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = 'X' # 방문처리
                    count+=1
                    queue.append([nx,ny])
    result.append(count) # 초콜릿 개수 기록
            

# 그룹별 초콜릿 개수 확인하기
def check(count):
    global box
    for i in range(len(box)):
        if box[i] == count:
            box[i] = -1 # 찾았다는 의미
            return False # 일치하는 값 발견
    return True # 불일치



for _ in range(int(input())):
    # 초콜릿 박스 현황 입력받기
    graph = [list(input()) for _ in range(3)]

    # 가운데 칸 데이터 입력받기
    data = list(map(int,input().split()))

    n = data[0]
    box = data[1:]
    
    # 그래프를 탐색하면서 'o'인 문자 발견시 bfs
    # 'O' 이외의 문자는 모두 방문한것으로 생각
    # 초콜릿이 한개도 없음에도, 숫자가 표시되어 있을 수 있음
    # 최종 결과를 비교해야함
    result = []
    for i in range(3):
        for j in range(3):
            if graph[i][j] == 'O':
                bfs(i,j) # 인접한 초콜릿 개수 저장
    
    result.sort()
    if result == box:
        print(1)
    else:
        print(0)