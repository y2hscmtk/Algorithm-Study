# 부분 수열의 합
n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

# 각 수열 원소를 한번 씩만 사용해야 함
# 거꾸로 DP
dp = [-1]*(m+1)
dp[0] = 0
for item in A:
    # 거꾸로 돌아가며 해당 아이템을 사용하여 원하는 수를 만드는 방법이 있는지 파악
    for j in range(m,-1,-1):
        if j-item >= 0 and dp[j-item] != -1:
            dp[j] = max(dp[j], dp[j-item] + 1)

if dp[m] == -1:
    print("No")
else:
    print("Yes")
