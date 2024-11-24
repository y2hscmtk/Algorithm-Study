# https://www.acmicpc.net/problem/10844
'''
N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''
n = int(input())
# dp[i][k] => 자리수가 i고, 앞자리가 k일때의 계단수의 개수
# 1<=k<=9, 1<=i<=100
dp = [[-1]*10 for _ in range(101)]
dp[1] = [1]*10

# depth : 현재 자리수
# num : 현재 자리수에서 가장 앞자리에 있는 수
def dfs(num,depth):
    if dp[depth][num] != -1: # depth 길이, 가장 앞자리 num이 이미 정의되어 있다면
        return dp[depth][num]
    if depth == 1: # 한자리수에 도달하였다면 경우는 모두 1개
        return 1
    plus,minus = 0,0
    if num<=8:
        plus = (dfs(num+1,depth-1)%1000000000)
    if num>=1:
        minus = (dfs(num-1,depth-1)%1000000000)
    dp[depth][num] = (plus + minus)%1000000000
    return dp[depth][num]

for i in range(1,10):
    # 자리수가 n이고 앞자리가 i인 수들의 합
    dfs(i,n)

print(sum(dp[n][1:])%1000000000)