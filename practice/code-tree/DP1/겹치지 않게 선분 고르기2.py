n = int(input())

points = [tuple(map(int,input().split())) for _ in range(n)] # n개의 선분 좌표 정보

points.sort() # 시작점을 기준으로 정렬

dp = [0]*n
dp[0] = 1 # 시작 좌표는 무조건 선택 가능

for i in range(n):
    # 현재 선분을 시작 선분으로 삼는 경우 초기값은 1
    dp[i] = 1

    # 이전에 선택한 선분과 현재 선분이 겹치지 않는 경우 중
    # 선택할 수 있는 최대 선분의 개수 계산
    x2,y2 = points[i] # 현재 선분
    for j in range(i):
        x1,y1 = points[j]

        # x2는 x1보다 무조건 앞서있음 - 정렬
        # x2가 y1보다 큰지만 확인하면 무조건 겹치지 않는 선분이 된다.
        if y1 < x2:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 큰 경우가 정답이 됨
ans = 0
for i in range(n):
    ans = max(ans,dp[i])

print(ans)