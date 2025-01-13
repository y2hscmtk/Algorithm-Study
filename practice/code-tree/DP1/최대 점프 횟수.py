# 조건에 맞게 선택적으로 전진하는 DP
# 최대 점프 횟수
'''
이전의 상황들 중에서 현재 위치로 점프 가능한 경우에 한하여 비교
dp[i] : i번째 위치에 도달할때 까지의 최대 점프 값

arr[n] : 현재 위치로부터 arr[n] 거리 만큼 점프 가능함 
'''
n = int(input())
arr = list(map(int, input().split()))

dp = [-1]*n # 처음부터 아예 도달하지 못하는 위치가 존재할 수 있음
dp[0] = 0 # 처음 위치에는 무조건 도달 가능함

for i in range(1,n):
    for j in range(i):
        # 현재 위치에 도달할 수 있는지 확인 필요
        if dp[j] == -1: # 처음위치에서 아예 도달하지 못할경우, j번째 위치에서 다음 위치로 점프 불가능
            continue
        # 점프가 가능한 거리인지 확인 필요
        # j위치에서 arr[j] 만큼 점프하면 i번째 위치에 확정적으로 도달 가능한지 확인
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1) # j번째 위치에서 점프 + 1, 현재까지의 최대값

# dp값들 중 최대값이 최대 점프 가능 횟수
ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)
