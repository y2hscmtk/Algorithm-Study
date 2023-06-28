# https://www.acmicpc.net/problem/13913
from collections import deque
'''
이동 경로를 저장하기 위한 배열을 생성
n에서 n+1로 이동하였다면 move[n+1]의 값에 n을 삽입한다
그리하여 나중에 거꾸로 거슬러 올라가며 이동경로를 파악할 수 있다.
'''
n,k = map(int,input().split())

# 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다 
# => 최대 배열의 크기 설정
visited  = [-1 for _ in range(100001)]
move = [-1 for _ in range(100001)] # 이동경로를 저장할 배열(해당 인덱스 이전에 방문한 좌표)


# 이동경로를 출력하는 함수
def printPath(): 
    global k
    # 어차피 k에 대한 이동경로를 출력할것이므로, 매개변수는 불필요
    array = []
    while k != n: # 출발지로 돌아올때까지 반복
        array.append(k)
        k = move[k] # 이전에 방문했던 좌표로 돌아가기
    # 목적지까지 되돌아갔다면, 시작 좌표 삽입후 뒤집어서 출력
    array.append(n)
    array.reverse()
    print(*array)


# 시작위치 n은 방문처리하고 목적지 k에 도달할때까지 bfs를 수행한다
def bfs():
    queue = deque()
    queue.append(n)
    visited [n] = 0 # 탐색 시작 좌표 방문처리
    while queue:
        x = queue.popleft() # 현재 좌표
        # 목적지에 도달하였다면 종료
        if x==k:
            print(visited[x])
            printPath()
            return # 함수 종료
        # 좌우로 이동하는 경우만 생각
        for nx in (2*x, x+1, x-1):
            if 0<=nx<100001 and visited[nx]==-1:
                queue.append(nx)
                visited[nx] = visited[x] + 1 # 1초 소요됨
                move[nx] = x # 이전경로 삽입
        
bfs()
