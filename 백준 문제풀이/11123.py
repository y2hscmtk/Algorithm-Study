# https://www.acmicpc.net/problem/11123

'''
#은 양 .은 들판, #이 두 개 이상 붙어있다면 양 무리가 된다.
몇개의 무리가 있는지 파악해라

첫 번째 줄은 테스트 케이스의 수를 나타나는 T를 입력받는다.

이후 각 테스트 케이스의 첫 번째 줄에서는 H,W 를 입력받는다. 

H는 그리드의 높이이고, W는 그리드의 너비이다. 이후 그리드의 높이 H 에 걸쳐서 W개의 문자로 이루어진 문자열 하나를 입력받는다. 

0 < T ≤ 100
0 < H, W ≤ 100
'''
'''
아이디어 : 
반복문을 이용해서 #를 만날때마다 방문한 공간인지 아닌지를 조사, #인데 아직 방문하지 않은 공간이 존재한다면 
새로운 그룹을 발견했다는 의미이고, BFS를 이용해서 인접한 공간에 있는 무리를 모두 방문처리한다.
반복이 종료된 후, 총 몇개의 그룹이 존재하는지 출력한다. 
'''
from collections import deque
t = int(input())

# 방향벡터 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# bfs정의
def bfs(s, e, visit):
    queue = deque()
    queue.append([s, e])  # 큐에 최초 탐색 좌표 삽입
    visit[s][e] = True  # 방문처리
    while queue:
        x, y = queue.popleft()
        # 네 방향에 대해 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지않으면서 방문한적 없는 좌표에 대해
            if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny]:
                if graph[nx][ny] == '#':  # 인접한 좌표가 '양'이라면
                    visit[nx][ny] = True  # 방문처리
                    queue.append([nx, ny])  # 인접좌표 큐에 삽입


for _ in range(t):
    h, w = map(int, input().split())
    # 그래프 입력받기
    graph = [list(input()) for _ in range(h)]
    # 방문정보를 저장할 배열 생성
    visit = [[False]*w for _ in range(h)]
    # 그룹 개수 0으로 초기화
    group_count = 0
    # 그룹 카운트 시작
    for i in range(h):
        for j in range(w):
            # 만약 '양'을 만났는데, 아직 탐색한적 없는 좌표라면
            # 그룹의 개수를 증가시키고, bfs를 진행하여 그룹이 어디까지 이루어져있는지 파악한다.
            if graph[i][j] == '#' and not visit[i][j]:
                group_count += 1  # 그룹 개수 증가
                bfs(i, j, visit)
    print(group_count)
