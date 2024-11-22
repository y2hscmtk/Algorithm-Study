# https://www.acmicpc.net/problem/11053
'''
dp[i] ; i번째 항에 대해서 가장 긴 부분 수열의 길이
'''
N = int(input())
A = list(map(int,input().split()))
dp = [-1]*N
dp[0] = 1 # 초기값 설정
for i in range(1,N):
    dp[i] = 1 # 연결되지 않더라도 자기 자신은 존재
    # 이전까지의 값들 중 현재 값보다 작은 값이 존재하는지 확인
    # 존재한다면 + 1
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))