# https://www.acmicpc.net/problem/14716
'''
상하좌우 대각선에 이어진 1을 하나의 글자로 간주
글자가 총 몇개인지 구하는 프로그램을 작성하라
'''
'''
visited배열을 만들고 처음 방문하는 1에 대하여 bfs를 실시하고 그룹의 개수를 늘린다.
1을 만났는데 이미 방문한 좌표일경우는 기존 그룹에 속해있다는 의미이므로 무시하고 넘어간다.
모든 배열의 원소를 이에 대해 탐색한후 정답을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
# 현수막 입력받기
graph = [list(map(int, input().split())) for _ in range(m)]
# 그룹의 개수(글자수) 초기화
group = 0
# 방문 정보를 저장할 배열 생성
visit = [[False]*n for _ in range(m)]

# 이동벡터 상하좌우대각선
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


# bfs 정의
def bfs(s, e):
    queue = deque()
    queue.append([s, e])
    visit[s][e] = True  # 방문처리
    while queue:
        x, y = queue.popleft()
        # 상하좌우대각선에 방문한적 없는 1이 있는지 검사
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않고, 방문한적 없는경우
            if 0 <= nx < m and 0 <= ny < n:
                # 해당 좌표가 1인 경우
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    # 방문처리후 큐에 삽입
                    visit[nx][ny] = True
                    queue.append([nx, ny])


for i in range(m):
    for j in range(n):
        # 탐색한적 없는 1을 찾았다면
        if graph[i][j] == 1 and not visit[i][j]:
            group += 1  # 그룹의 개수를 늘리고
            bfs(i, j)  # 그룹의 멤버를 파악한다. => 모두 방문처리

# 정답
print(group)
