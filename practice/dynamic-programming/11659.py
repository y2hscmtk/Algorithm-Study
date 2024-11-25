# https://www.acmicpc.net/problem/11659
'''
접근 2 : Top-down DP
메모리 초과 => O(N^2)이므로 N의 크기가 크면 시간초과 발생
'''
import sys
def sol2():
    sys.setrecursionlimit(100001)
    N, M = map(int,input().split())
    data = [0] + list(map(int,input().split()))
    dp = [[-1]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = data[i]

    # i부터 j까지의 합
    def recursion(i,j):
        if dp[i][j] != -1: # i부터 j까지의 합이 기록되어 있다면
            return dp[i][j]
        if j == i: # 가장 아래까지 도달하였다면
            return dp[i][j]
        # j번째 수 + 이전에 기록된 수
        dp[i][j] = data[j] + recursion(i,j-1)
        return dp[i][j]

    for _ in range(M):
        i,j = map(int,input().split())
        print(recursion(i,j))

# https://www.acmicpc.net/problem/11659
'''
접근 1 : 누적합 배열을 생성하여 각 합을 미리 기록해두기
'''
def sol1():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    data = [0] + list(map(int,input().split()))
    dp = [0]*(N+1)
    for i in range(1,N+1):
        dp[i] = dp[i-1] + data[i]
    for _ in range(M):
        i,j = map(int,input().split())
        print(dp[j] - dp[i-1])
sol1()