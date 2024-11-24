# https://www.acmicpc.net/problem/2748
'''
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하기 (n<=90)
'''
dp = [0]*91
dp[0],dp[1] = 0,1
for i in range(2,91):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[int(input())])