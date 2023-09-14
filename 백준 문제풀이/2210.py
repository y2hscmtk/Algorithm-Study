# https://www.acmicpc.net/problem/2210

'''
5×5 크기의 숫자판
임의의 위치에서 탐색을 시작하여 상하좌우로 5번 이동하면 종료,
이동하면서 만나게 되는 숫자들 저장필요 => 최종적으로 set에 저장해야 함
set()자료형을 활용하여 같은 숫자가 들어가는 경우 방지
갔던 길을 다시 오갈수있음
만들 수 있는 모든 경우의 수 출력
'''
from collections import deque

result = set()

# 방향 벡터 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 문자열로 5x5 크기의 맵 입력받기
graph = list(input().split() for _ in range(5))


def bfs(s,e):
    global result # 만들 수 있는 모든 숫자 저장
    queue = deque()
    # 탐색의 시작 좌표 큐에 삽입
    # 세번째 인자는 탐색하며 만들어진 숫자 정보(string)
    queue.append([s,e,graph[s][e]]) 
    while queue:
        x, y,curr_number = queue.popleft() # 현재 노드,현재까지 만들어진 숫자
        # 현재 시점에서 글자의 길이가 6인지 파악
        # 만약 6이라면 set()에 삽입하고 해당 시점에서는 더이상 bfs를 수행하지 않음
        if len(curr_number) == 6:
            result.add(curr_number) # set에 만들어진 숫자 삽입하고
            continue # 현재 시점에서 더이상 bfs를 이어가지 않음
        for i in range(4): # 네 방향에 대해서
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않는지 확인
            if 0<=nx<5 and 0<=ny<5:
                queue.append([nx,ny,curr_number+graph[nx][ny]])

# 모든 좌표에 대해서 bfs수행 => 임의의 위치에서 숫자만들기를 시작한다
for i in range(5):
    for j in range(5):
        bfs(i,j)

# 탐색결과 만들어진 정답 출력
print(len(result))
        

