# https://www.acmicpc.net/problem/10211
'''
다이니막 프로그래밍
더했을때 이득이 되는지, 손해가 되는지 계산하여 이득이 되는경우만 부분수열로 생각
손해가 된다면 해당 부분에서부터 다시 부분수열로 생각하여 누적합 계산
'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = numbers[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1]+numbers[i], numbers[i])
    print(max(dp))  # dp테이블에서의 최대값이 문제의 정답
