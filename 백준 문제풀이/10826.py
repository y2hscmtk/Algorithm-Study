# https://www.acmicpc.net/problem/10826
'''
n번째 피보나치 수를 구하는 프로그램 작성
'''
n = int(input())

# dp테이블 생성
dp = [-1 for i in range(n+1)]

# 피보나치 메모이제이션
for i in range(n+1):
    # 기본값 작성
    if i == 0 or i == 1:
        dp[i] = i
        continue
    if dp[i] == -1:  # 아직 피보나치 수가 기록되어 있지않다면
        dp[i] = dp[i-1] + dp[i-2]  # 값 기록

print(dp[n])
