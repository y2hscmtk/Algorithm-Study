# 증가했다가 감소하는 부분 수열
# 풀이 참조
n = int(input())
sequence = list(map(int, input().split()))

dp_max = [1] * n  # 증가하는 수열
dp_min = [1] * n  # 감소하는 수열

# 증가하는 부분 수열 (LIS) 계산
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp_max[i] = max(dp_max[i], dp_max[j] + 1)

# 감소하는 부분 수열 (LDS) 계산 - 거꾸로
# dp_min[i] : i번째 이후로 감소하는 수열의 최장 길이
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if sequence[j] < sequence[i]:
            dp_min[i] = max(dp_min[i], dp_min[j] + 1)

# 증가-감소 부분 수열의 최대 길이 계산
ans = 0
for i in range(n):
    # 증가 후 감소하는 경우
    ans = max(ans, dp_max[i] + dp_min[i] - 1)

print(ans)