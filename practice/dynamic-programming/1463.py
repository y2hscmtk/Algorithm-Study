# https://www.acmicpc.net/problem/1463
'''
숫자 N에 대해서 top-down 으로 3가지 연산 수행
dp[1] = 0, dp[2] = 1, dp[3] = 1 # 초기값 기록
재귀수행 과정 중에 1이 되었다면 dp테이블 업데이트 후 탈출
dp[i] => i가 1이 되기 위해 필요한 최소 연산의 횟수
'''
N = int(input())
# solve 1
from collections import deque
visited = [-1]*(N+1)
def bfs():
    queue = deque()
    queue.append(1)
    # 1. 3을 곱하던가, 2를 곱하던가, 1을 더해주면됨
    visited[1] = 0
    while queue:
        x = queue.popleft()
        if x == N:
            return visited[x]
        for nx in (x*3,x*2,x+1):
            if 1<=nx<=N and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
print(bfs())

# solve 2
dp = [0]*(N+1)
for i in range(2,N+1):
    # 1을 빼는 연산의 경우
    dp[i] = dp[i-1] + 1
    # 3으로 나누는 연산의 경우
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3] + 1) # 연산이 수행되었으므로 이전 최소 연산(dp[i//3]) + 1 
    # 2로 나는 연산의 경우
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2] + 1)

print(dp[N])