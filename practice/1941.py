# https://www.acmicpc.net/problem/1941
'''
2차원 배열에 배치된 학생을 1차원에 존재한다고 생각
dfs를 통해 각 번호의 학생에 대해서
1. 7명을 모았는지
2. S가 4명 이상인지
를 판단한 후
bfs를 통해 각 학생들이 인접해 있는지 판단하여, 인접해 있다면 그룹화가 가능한 것으로 생각하여 정답 +1
'''
from collections import deque
dx = [0,0,-1,1]; dy = [-1,1,0,0]
students = [input() for _ in range(5)]
v = [[0]*5 for _ in range(5)] # 해당 좌표의 학생이 7공주로 선택되었는지 아닌지 여부
ans = 0 # 가능한 경우의 수(정답)

def bfs(si,sj):
    visited = [[False]*5 for _ in range(5)]
    visited[si][sj] = True # 시작 좌표 방문 처리
    cnt = 1 # 인접한 학생의 수가 7명인지 파악
    queue = deque()
    queue.append((si,sj))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 범위를 벗어나지 않으면서, 방문한적 없으면서, 인접 학생이 7공주로 선택되었다면
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and v[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt+=1
    return cnt == 7 # 인접한 학생 수가 7명이라면 True 아니면 False


# 배열을 돌면서 7공주 만날 경우, bfs돌면서 7명이 모두 인접한지 파악
def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i,j)


# 0~24번 학생, 해당 학생을 7공주로 선택할지 말지, 현재까지 선택된 그룹에서 S가 몇명인지
def dfs(n, cnt, scnt):
    global ans
    # 가지치기
    if cnt>7: # 7공주 불가
        return
    if n == 25: # 마지막 학생까지 비교완료
        # 7명 구성 완료, 이다솜 파 학생 4명 이상인 경우
        if cnt == 7 and scnt >=4:
            if check(): # 인접한 그룹인 경우
                ans += 1
        return
    # n번째 학생을 7공주로 선택하는 경우
    v[n//5][n%5] = 1 # 선택
    dfs(n+1,cnt+1,scnt+int(students[n//5][n%5]=='S'))
    v[n//5][n%5] = 0 # 선택 x
    # n번째 학생을 7공주로 선택하지 않는 경우
    dfs(n+1,cnt,scnt)

dfs(0,0,0)
print(ans)