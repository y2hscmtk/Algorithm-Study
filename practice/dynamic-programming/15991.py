# https://www.acmicpc.net/problem/15991
'''
풀이 참조
대칭이 되는 방법
1 + 대칭수 + 1 => dp[i-2] ; 2(1+1)는 보유, 추가로 필요한 수는 i-2
2 + 대칭수 + 2 => dp[i-4] ; 4(2+2)는 보유, 추가로 필요한 수는 i-4
3 + 대칭수 + 3 => dp[i-6] ; 6(3+3)는 보유, 추가로 필요한 수는 i-6
'''
import sys
input = sys.stdin.readline

dp = [0]*100001
dp[0],dp[1],dp[2],dp[3],dp[4],dp[5],dp[6] = 0,1,2,2,3,3,6
for i in range(7,100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6])%1000000009

for i in range(int(input())):
    print(dp[int(input())])
