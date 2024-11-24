# https://www.acmicpc.net/problem/2156
'''
1,2번째 칸의 수는 현재 술잔을 마시는 경우가 최대
3번째 칸의 경우 1번째 칸을 마시거나, 2번째 칸을 마시고 3번째 칸을 마시는 경우가 최대
연속된 술잔을 선택하지 않는 조건에서 최대값 + 현재 값
(1 ≤ n ≤ 10,000) 
'''
n = int(input())
data = [0]*10001
dp = [0]*10001
for i in range(1,n+1):
    data[i] = int(input())
for i in range(1,n+1):
    if i == 1:
        dp[i] = data[i]
    elif i == 2:
        dp[i] = data[i-1] + data[i]
    else:
        # 2개전 잔을 선택하고, 현재 잔을 선택하는 경우
        # 3개전 잔과, 1개전 잔을 선택하고 현재 잔을 선택하는 경우
        dp[i] = max(max(dp[:i-2])+data[i-1],dp[i-2]) + data[i]
print(max(dp))