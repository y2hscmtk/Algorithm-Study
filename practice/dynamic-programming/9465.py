# https://www.acmicpc.net/problem/9465
'''
열 단위로 생각
현재 열에서 숫자를 고르지 않을 경우 다음 열에서 어떤 숫자를 고르던지 자유
'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = [[0] + list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1],dp[1][1] = data[0][1],data[1][1]
    for i in range(2,n+1):
        # 이전 열에서 숫자를 고르지 않았을 경우
        # -> 두열 전에서 최대 값 + 현재수에서 각 자리 수
        # 이전 열에서 숫자를 고르고, 현재 수에서 조건에 맞는 수를 고르는 경우
        for j in range(2):
            dp[j][i] = max(max(dp[j][i-2],dp[1-j][i-2]) + data[j][i], dp[1-j][i-1] + data[j][i])
    
    # 마지막 줄 기준 둘 중 최대값 출력
    print(max(dp[0][n],dp[1][n]))